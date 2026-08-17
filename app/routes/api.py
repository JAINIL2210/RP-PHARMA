from flask import Blueprint, jsonify, request
from app.models import db, Product, Category, SiteSetting, Enquiry

api_bp = Blueprint('api', __name__)

@api_bp.route('/products')
def get_products():
    """API endpoint to get filterable products list."""
    query = Product.query.filter_by(is_active=True)
    
    # Filter by Type
    prod_type = request.args.get('type', '').strip().lower()
    if prod_type in ['pharmaceutical', 'nutraceutical']:
        query = query.filter(Product.type == prod_type)
        
    # Filter by Category
    category_slug = request.args.get('category', '').strip()
    if category_slug:
        cat = Category.query.filter_by(slug=category_slug).first()
        if cat:
            query = query.filter(Product.category_id == cat.id)
            
    # Filter by Dosage Form
    dosage = request.args.get('dosage_form', '').strip()
    if dosage:
        query = query.filter(Product.dosage_form.ilike(f"%{dosage}%"))
        
    # Search
    search = request.args.get('search', '').strip()
    if search:
        pattern = f"%{search}%"
        query = query.filter(
            db.or_(
                Product.name.ilike(pattern),
                Product.composition.ilike(pattern),
                Product.indications.ilike(pattern)
            )
        )
        
    products = query.order_by(Product.name.asc()).all()
    return jsonify({
        'success': True,
        'count': len(products),
        'products': [p.to_dict() for p in products]
    })

@api_bp.route('/products/<int:product_id>')
def get_product(product_id):
    """API endpoint to get a single product details."""
    product = Product.query.filter_by(id=product_id, is_active=True).first()
    if not product:
        return jsonify({'success': False, 'message': 'Product not found'}), 404
        
    return jsonify({
        'success': True,
        'product': product.to_dict()
    })

@api_bp.route('/categories')
def get_categories():
    """API endpoint to get all active categories."""
    categories = Category.query.filter_by(is_active=True).order_by(Category.display_order).all()
    return jsonify({
        'success': True,
        'categories': [c.to_dict() for c in categories]
    })

@api_bp.route('/settings')
def get_settings():
    """API endpoint to get public company configuration."""
    settings = SiteSetting.query.all()
    data = {s.key: s.value for s in settings}
    return jsonify({
        'success': True,
        'settings': data
    })
