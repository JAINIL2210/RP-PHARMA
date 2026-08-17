from flask import Blueprint, render_template, request, abort
from app.models import db, Product, Category

products_bp = Blueprint('products', __name__)

@products_bp.route('/pharmaceuticals')
def pharmaceuticals():
    """Dedicated Pharmaceuticals overview page with segment categories and featured formulations."""
    categories = Category.query.filter_by(type='pharmaceutical', is_active=True).order_by(Category.display_order).all()
    featured_products = Product.query.filter_by(type='pharmaceutical', is_active=True).limit(6).all()
    
    return render_template(
        'pharmaceuticals.html',
        categories=categories,
        featured_products=featured_products
    )

@products_bp.route('/nutraceuticals')
def nutraceuticals():
    """Dedicated Nutraceuticals overview page with wellness categories and products."""
    categories = Category.query.filter_by(type='nutraceutical', is_active=True).order_by(Category.display_order).all()
    featured_products = Product.query.filter_by(type='nutraceutical', is_active=True).limit(6).all()
    
    return render_template(
        'nutraceuticals.html',
        categories=categories,
        featured_products=featured_products
    )

@products_bp.route('/products')
def list_products():
    """Searchable & Filterable Product Catalogue."""
    query = Product.query.filter_by(is_active=True)
    
    # Filter by Product Type (pharmaceutical / nutraceutical)
    type_filter = request.args.get('type', '').strip().lower()
    if type_filter in ['pharmaceutical', 'nutraceutical']:
        query = query.filter(Product.type == type_filter)
        
    # Filter by Category
    category_slug = request.args.get('category', '').strip()
    selected_category = None
    if category_slug:
        selected_category = Category.query.filter_by(slug=category_slug).first()
        if selected_category:
            query = query.filter(Product.category_id == selected_category.id)
            
    # Filter by Dosage Form
    dosage_form = request.args.get('dosage_form', '').strip()
    if dosage_form:
        query = query.filter(Product.dosage_form.ilike(f"%{dosage_form}%"))
        
    # Search by keyword (Name, Composition, Indications)
    search_keyword = request.args.get('search', '').strip()
    if search_keyword:
        search_pattern = f"%{search_keyword}%"
        query = query.filter(
            db.or_(
                Product.name.ilike(search_pattern),
                Product.composition.ilike(search_pattern),
                Product.indications.ilike(search_pattern)
            )
        )
        
    products = query.order_by(Product.name.asc()).all()
    
    # Fetch all categories and distinct dosage forms for filter sidebars
    all_categories = Category.query.filter_by(is_active=True).order_by(Category.name.asc()).all()
    pharma_categories = [c for c in all_categories if c.type == 'pharmaceutical']
    nutra_categories = [c for c in all_categories if c.type == 'nutraceutical']
    
    # Get distinct dosage forms
    distinct_forms = db.session.query(Product.dosage_form).filter_by(is_active=True).distinct().all()
    dosage_forms = sorted(list(set([form[0] for form in distinct_forms if form[0]])))

    return render_template(
        'products/list.html',
        products=products,
        pharma_categories=pharma_categories,
        nutra_categories=nutra_categories,
        dosage_forms=dosage_forms,
        selected_type=type_filter,
        selected_category=selected_category,
        selected_dosage=dosage_form,
        search_keyword=search_keyword,
        total_count=len(products)
    )

@products_bp.route('/product/<slug>')
def product_detail(slug):
    """Detailed specifications and technical profile for a single product."""
    product = Product.query.filter_by(slug=slug, is_active=True).first()
    if not product:
        # Check by numeric ID if slug lookup fails
        if slug.isdigit():
            product = Product.query.filter_by(id=int(slug), is_active=True).first()
            
    if not product:
        abort(404)
        
    # Related products from same category
    related_products = Product.query.filter(
        Product.category_id == product.category_id,
        Product.id != product.id,
        Product.is_active == True
    ).limit(3).all()
    
    return render_template(
        'products/detail.html',
        product=product,
        related_products=related_products
    )
