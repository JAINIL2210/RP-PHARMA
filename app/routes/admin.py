import os
import csv
import io
import uuid
from functools import wraps
from datetime import datetime, timezone
from flask import (
    Blueprint, render_template, request, redirect, url_for,
    flash, session, current_app, Response, jsonify
)
from werkzeug.utils import secure_filename
from app.models import db, AdminUser, Product, Category, Enquiry, SiteSetting, slugify

admin_bp = Blueprint('admin', __name__)

def login_required(f):
    """Decorator to protect admin routes."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin_user_id' not in session:
            flash('Please log in to access the administration panel.', 'warning')
            return redirect(url_for('admin.login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

# ----------------- AUTHENTICATION -----------------

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Admin login page."""
    if 'admin_user_id' in session:
        return redirect(url_for('admin.dashboard'))
        
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()
        
        user = AdminUser.query.filter_by(username=username).first()
        if user and user.is_active and user.check_password(password):
            session['admin_user_id'] = user.id
            session['admin_username'] = user.username
            session['admin_role'] = user.role
            user.last_login = datetime.now(timezone.utc)
            db.session.commit()
            
            flash(f'Welcome back, {user.username}!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page or url_for('admin.dashboard'))
        else:
            flash('Invalid username or password.', 'danger')
            
    return render_template('admin/login.html')

@admin_bp.route('/logout')
def logout():
    """Admin logout."""
    session.clear()
    flash('You have been securely logged out.', 'info')
    return redirect(url_for('admin.login'))

# ----------------- DASHBOARD -----------------

@admin_bp.route('/')
@admin_bp.route('/dashboard')
@login_required
def dashboard():
    """Admin dashboard overview."""
    total_products = Product.query.count()
    pharma_count = Product.query.filter_by(type='pharmaceutical').count()
    nutra_count = Product.query.filter_by(type='nutraceutical').count()
    total_enquiries = Enquiry.query.count()
    new_enquiries_count = Enquiry.query.filter_by(status='new').count()
    
    recent_enquiries = Enquiry.query.order_by(Enquiry.created_at.desc()).limit(6).all()
    recent_products = Product.query.order_by(Product.created_at.desc()).limit(5).all()
    
    return render_template(
        'admin/dashboard.html',
        total_products=total_products,
        pharma_count=pharma_count,
        nutra_count=nutra_count,
        total_enquiries=total_enquiries,
        new_enquiries_count=new_enquiries_count,
        recent_enquiries=recent_enquiries,
        recent_products=recent_products
    )

# ----------------- PRODUCTS MANAGEMENT -----------------

@admin_bp.route('/products')
@login_required
def products_list():
    """List all products with filters."""
    query = Product.query
    
    # Filter by type
    type_filter = request.args.get('type', '').strip()
    if type_filter in ['pharmaceutical', 'nutraceutical']:
        query = query.filter_by(type=type_filter)
        
    # Filter by category
    cat_id = request.args.get('category_id', '').strip()
    if cat_id.isdigit():
        query = query.filter_by(category_id=int(cat_id))
        
    # Search
    search = request.args.get('search', '').strip()
    if search:
        query = query.filter(
            db.or_(
                Product.name.ilike(f"%{search}%"),
                Product.composition.ilike(f"%{search}%")
            )
        )
        
    products = query.order_by(Product.created_at.desc()).all()
    categories = Category.query.order_by(Category.name.asc()).all()
    
    return render_template(
        'admin/products_list.html',
        products=products,
        categories=categories,
        selected_type=type_filter,
        selected_category=cat_id,
        search_query=search
    )

@admin_bp.route('/products/add', methods=['GET', 'POST'])
@login_required
def product_add():
    """Add a new pharmaceutical or nutraceutical product."""
    categories = Category.query.filter_by(is_active=True).order_by(Category.name.asc()).all()
    
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        prod_type = request.form.get('type', 'pharmaceutical').strip()
        category_id = request.form.get('category_id')
        composition = request.form.get('composition', '').strip()
        dosage_form = request.form.get('dosage_form', '').strip()
        strength = request.form.get('strength', '').strip()
        packaging = request.form.get('packaging', '').strip()
        description = request.form.get('description', '').strip()
        indications = request.form.get('indications', '').strip()
        available_markets = request.form.get('available_markets', '').strip()
        dossier_status = request.form.get('dossier_status', '').strip()
        stability_status = request.form.get('stability_status', '').strip()
        validation_status = request.form.get('validation_status', '').strip()
        is_featured = bool(request.form.get('is_featured'))
        is_active = bool(request.form.get('is_active'))
        
        if not name or not composition or not dosage_form or not category_id:
            flash('Please fill in all required fields (Name, Category, Composition, Dosage Form).', 'danger')
            return render_template('admin/product_form.html', categories=categories, product=None)
            
        # Generate Slug
        base_slug = slugify(name)
        slug = base_slug
        counter = 1
        while Product.query.filter_by(slug=slug).first():
            slug = f"{base_slug}-{counter}"
            counter += 1
            
        # Handle Image Upload
        image_url = None
        if 'image' in request.files:
            img_file = request.files['image']
            if img_file and img_file.filename != '':
                ext = img_file.filename.rsplit('.', 1)[-1].lower()
                if ext in current_app.config['ALLOWED_IMAGE_EXTENSIONS']:
                    filename = f"prod_{uuid.uuid4().hex[:8]}_{secure_filename(img_file.filename)}"
                    upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], 'products', filename)
                    img_file.save(upload_path)
                    image_url = f"/static/uploads/products/{filename}"

        product = Product(
            name=name,
            slug=slug,
            type=prod_type,
            category_id=int(category_id),
            composition=composition,
            dosage_form=dosage_form,
            strength=strength,
            packaging=packaging,
            description=description,
            indications=indications,
            available_markets=available_markets or 'Asia, Africa, Middle East, CIS, Latin America',
            dossier_status=dossier_status or 'CTD Dossier Available on Request',
            stability_status=stability_status or 'Zone IVb Stability Data Available',
            validation_status=validation_status or 'Process & Analytical Validation Complete',
            image_url=image_url,
            is_featured=is_featured,
            is_active=is_active
        )
        
        db.session.add(product)
        db.session.commit()
        
        flash(f'Product "{name}" added successfully!', 'success')
        return redirect(url_for('admin.products_list'))
        
    return render_template('admin/product_form.html', categories=categories, product=None)

@admin_bp.route('/products/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def product_edit(id):
    """Edit existing product."""
    product = Product.query.get_or_404(id)
    categories = Category.query.filter_by(is_active=True).order_by(Category.name.asc()).all()
    
    if request.method == 'POST':
        product.name = request.form.get('name', '').strip()
        product.type = request.form.get('type', 'pharmaceutical').strip()
        product.category_id = int(request.form.get('category_id'))
        product.composition = request.form.get('composition', '').strip()
        product.dosage_form = request.form.get('dosage_form', '').strip()
        product.strength = request.form.get('strength', '').strip()
        product.packaging = request.form.get('packaging', '').strip()
        product.description = request.form.get('description', '').strip()
        product.indications = request.form.get('indications', '').strip()
        product.available_markets = request.form.get('available_markets', '').strip()
        product.dossier_status = request.form.get('dossier_status', '').strip()
        product.stability_status = request.form.get('stability_status', '').strip()
        product.validation_status = request.form.get('validation_status', '').strip()
        product.is_featured = bool(request.form.get('is_featured'))
        product.is_active = bool(request.form.get('is_active'))
        
        # Handle Image Upload if changed
        if 'image' in request.files:
            img_file = request.files['image']
            if img_file and img_file.filename != '':
                ext = img_file.filename.rsplit('.', 1)[-1].lower()
                if ext in current_app.config['ALLOWED_IMAGE_EXTENSIONS']:
                    filename = f"prod_{uuid.uuid4().hex[:8]}_{secure_filename(img_file.filename)}"
                    upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], 'products', filename)
                    img_file.save(upload_path)
                    product.image_url = f"/static/uploads/products/{filename}"

        db.session.commit()
        flash(f'Product "{product.name}" updated successfully!', 'success')
        return redirect(url_for('admin.products_list'))
        
    return render_template('admin/product_form.html', categories=categories, product=product)

@admin_bp.route('/products/delete/<int:id>', methods=['POST'])
@login_required
def product_delete(id):
    """Delete a product."""
    product = Product.query.get_or_404(id)
    name = product.name
    db.session.delete(product)
    db.session.commit()
    flash(f'Product "{name}" has been deleted.', 'info')
    return redirect(url_for('admin.products_list'))

# ----------------- CATEGORIES MANAGEMENT -----------------

@admin_bp.route('/categories', methods=['GET', 'POST'])
@login_required
def categories_list():
    """Manage product categories."""
    if request.method == 'POST':
        action = request.form.get('action', 'add')
        
        if action == 'add':
            name = request.form.get('name', '').strip()
            cat_type = request.form.get('type', 'pharmaceutical').strip()
            description = request.form.get('description', '').strip()
            icon = request.form.get('icon', 'fa-pills').strip()
            display_order = int(request.form.get('display_order', 0))
            
            if name:
                slug = slugify(name)
                cat = Category(
                    name=name,
                    slug=slug,
                    type=cat_type,
                    description=description,
                    icon=icon,
                    display_order=display_order,
                    is_active=True
                )
                db.session.add(cat)
                db.session.commit()
                flash(f'Category "{name}" added successfully!', 'success')
                
        elif action == 'edit':
            cat_id = request.form.get('category_id')
            cat = Category.query.get(cat_id)
            if cat:
                cat.name = request.form.get('name', '').strip()
                cat.type = request.form.get('type', 'pharmaceutical').strip()
                cat.description = request.form.get('description', '').strip()
                cat.icon = request.form.get('icon', 'fa-pills').strip()
                cat.display_order = int(request.form.get('display_order', 0))
                cat.is_active = bool(request.form.get('is_active'))
                db.session.commit()
                flash(f'Category "{cat.name}" updated successfully!', 'success')
                
        elif action == 'delete':
            cat_id = request.form.get('category_id')
            cat = Category.query.get(cat_id)
            if cat:
                name = cat.name
                db.session.delete(cat)
                db.session.commit()
                flash(f'Category "{name}" deleted.', 'info')
                
        return redirect(url_for('admin.categories_list'))

    categories = Category.query.order_by(Category.type.asc(), Category.display_order.asc()).all()
    return render_template('admin/categories_list.html', categories=categories)

# ----------------- ENQUIRIES MANAGEMENT -----------------

@admin_bp.route('/enquiries')
@login_required
def enquiries_list():
    """List customer enquiries with status filtering."""
    status_filter = request.args.get('status', '').strip()
    query = Enquiry.query
    
    if status_filter in ['new', 'in_review', 'contacted', 'closed']:
        query = query.filter_by(status=status_filter)
        
    search = request.args.get('search', '').strip()
    if search:
        query = query.filter(
            db.or_(
                Enquiry.full_name.ilike(f"%{search}%"),
                Enquiry.company_name.ilike(f"%{search}%"),
                Enquiry.email.ilike(f"%{search}%"),
                Enquiry.country.ilike(f"%{search}%"),
                Enquiry.product_name.ilike(f"%{search}%")
            )
        )
        
    enquiries = query.order_by(Enquiry.created_at.desc()).all()
    return render_template(
        'admin/enquiries_list.html',
        enquiries=enquiries,
        selected_status=status_filter,
        search_query=search
    )

@admin_bp.route('/enquiries/<int:id>', methods=['GET', 'POST'])
@login_required
def enquiry_detail(id):
    """View enquiry details and update review status/notes."""
    enquiry = Enquiry.query.get_or_404(id)
    
    if request.method == 'POST':
        enquiry.status = request.form.get('status', enquiry.status)
        enquiry.admin_notes = request.form.get('admin_notes', enquiry.admin_notes)
        db.session.commit()
        flash('Enquiry status updated successfully.', 'success')
        return redirect(url_for('admin.enquiry_detail', id=enquiry.id))
        
    return render_template('admin/enquiry_detail.html', enquiry=enquiry)

@admin_bp.route('/enquiries/delete/<int:id>', methods=['POST'])
@login_required
def enquiry_delete(id):
    """Delete an enquiry."""
    enquiry = Enquiry.query.get_or_404(id)
    db.session.delete(enquiry)
    db.session.commit()
    flash('Enquiry deleted successfully.', 'info')
    return redirect(url_for('admin.enquiries_list'))

@admin_bp.route('/enquiries/export')
@login_required
def enquiries_export_csv():
    """Export all enquiries to CSV file."""
    si = io.StringIO()
    cw = csv.writer(si)
    
    # Headers
    cw.writerow([
        'ID', 'Type', 'Full Name', 'Company Name', 'Business Type',
        'Email', 'Phone', 'Country', 'Product/Interest', 'Category',
        'Message', 'Status', 'Date Received'
    ])
    
    enquiries = Enquiry.query.order_by(Enquiry.created_at.desc()).all()
    for e in enquiries:
        cw.writerow([
            e.id,
            e.enquiry_type,
            e.full_name,
            e.company_name or '',
            e.business_type or '',
            e.email,
            e.phone or '',
            e.country or '',
            e.product_name or '',
            e.category or '',
            e.message.replace('\n', ' ') if e.message else '',
            e.status,
            e.created_at.strftime('%Y-%m-%d %H:%M') if e.created_at else ''
        ])
        
    output = si.getvalue()
    response = Response(output, mimetype='text/csv')
    response.headers['Content-Disposition'] = f'attachment; filename=rp_pharma_enquiries_{datetime.now(timezone.utc).strftime("%Y%m%d")}.csv'
    return response

# ----------------- SETTINGS MANAGEMENT -----------------

@admin_bp.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    """Update dynamic website settings (contact placeholders, trust metrics, socials)."""
    if request.method == 'POST':
        for key in request.form:
            if key != 'csrf_token':
                val = request.form.get(key, '').strip()
                SiteSetting.set_value(key, val)
                
        flash('Website settings saved successfully!', 'success')
        return redirect(url_for('admin.settings'))
        
    all_settings = SiteSetting.query.order_by(SiteSetting.group, SiteSetting.key).all()
    settings_by_group = {}
    for s in all_settings:
        settings_by_group.setdefault(s.group, []).append(s)
        
    return render_template('admin/settings.html', settings_by_group=settings_by_group)
