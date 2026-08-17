from flask import Blueprint, render_template, make_response, current_app, request
from app.models import Category, Product, SiteSetting

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """Home page route with hero, trust stats, pharma & nutra highlights, quality & global presence previews."""
    featured_pharma = Product.query.filter_by(type='pharmaceutical', is_featured=True, is_active=True).limit(4).all()
    featured_nutra = Product.query.filter_by(type='nutraceutical', is_featured=True, is_active=True).limit(4).all()
    pharma_categories = Category.query.filter_by(type='pharmaceutical', is_active=True).order_by(Category.display_order).all()
    nutra_categories = Category.query.filter_by(type='nutraceutical', is_active=True).order_by(Category.display_order).all()
    
    return render_template(
        'index.html',
        featured_pharma=featured_pharma,
        featured_nutra=featured_nutra,
        pharma_categories=pharma_categories,
        nutra_categories=nutra_categories
    )

@main_bp.route('/about')
def about():
    """About Us page: Company background, Vision, Mission, Core Values, Technical & Regulatory capabilities."""
    return render_template('about.html')

@main_bp.route('/quality')
def quality():
    """Quality & Compliance page: QA/QC, WHO-GMP & EU-GMP partner framework, Dossiers, Stability, Validation."""
    return render_template('quality.html')

@main_bp.route('/manufacturing')
def manufacturing():
    """Manufacturing page: 7-step ecosystem, qualified manufacturing partner facilities across India."""
    return render_template('manufacturing.html')

@main_bp.route('/global-presence')
def global_presence():
    """Global Presence page: Interactive international map, emerging markets, distributor partnership portal."""
    return render_template('global_presence.html')

@main_bp.route('/business-enquiry')
def business_enquiry():
    """B2B Business Enquiry page: Partnership form for Distributors, Importers, Wholesalers."""
    categories = Category.query.filter_by(is_active=True).order_by(Category.name).all()
    return render_template('business_enquiry.html', categories=categories)

@main_bp.route('/contact')
def contact():
    """Contact Us page: Corporate details placeholders, office info, quick inquiry form."""
    return render_template('contact.html')

@main_bp.route('/privacy-policy')
def privacy_policy():
    """Privacy Policy page."""
    return render_template('privacy.html')

@main_bp.route('/terms')
def terms():
    """Terms & Conditions page."""
    return render_template('terms.html')

@main_bp.route('/sitemap.xml')
def sitemap():
    """Dynamic XML Sitemap for SEO."""
    host = request.host_url.rstrip('/')
    static_urls = [
        f"{host}/",
        f"{host}/about",
        f"{host}/pharmaceuticals",
        f"{host}/nutraceuticals",
        f"{host}/products",
        f"{host}/quality",
        f"{host}/manufacturing",
        f"{host}/global-presence",
        f"{host}/business-enquiry",
        f"{host}/contact",
        f"{host}/privacy-policy",
        f"{host}/terms"
    ]
    
    products = Product.query.filter_by(is_active=True).all()
    product_urls = [f"{host}/product/{p.slug}" for p in products]
    
    categories = Category.query.filter_by(is_active=True).all()
    category_urls = [f"{host}/products?category={c.slug}" for c in categories]
    
    all_urls = static_urls + product_urls + category_urls
    
    sitemap_xml = ['<?xml version="1.0" encoding="UTF-8"?>']
    sitemap_xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    
    for url in all_urls:
        sitemap_xml.append('  <url>')
        sitemap_xml.append(f'    <loc>{url}</loc>')
        sitemap_xml.append('    <changefreq>weekly</changefreq>')
        sitemap_xml.append('    <priority>0.8</priority>')
        sitemap_xml.append('  </url>')
        
    sitemap_xml.append('</urlset>')
    
    response = make_response('\n'.join(sitemap_xml))
    response.headers['Content-Type'] = 'application/xml'
    return response

@main_bp.route('/robots.txt')
def robots():
    """Robots.txt for web crawlers."""
    host = request.host_url.rstrip('/')
    content = f"""User-agent: *
Allow: /
Disallow: /admin/
Disallow: /api/

Sitemap: {host}/sitemap.xml
"""
    response = make_response(content)
    response.headers['Content-Type'] = 'text/plain'
    return response
