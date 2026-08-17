from datetime import datetime, timezone
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
import re

db = SQLAlchemy()

def utcnow():
    return datetime.now(timezone.utc)

def slugify(text):
    """Generate clean URL slug from string."""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    return text.strip('-')

class AdminUser(db.Model):
    """Admin user model for dashboard authentication."""
    __tablename__ = 'admin_users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(30), default='admin')
    is_active = db.Column(db.Boolean, default=True)
    last_login = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=utcnow)
    
    def set_password(self, password):
        """Hash and set the user's password."""
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        """Verify user's password against hash."""
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<AdminUser {self.username}>'


class Category(db.Model):
    """Category model for Pharmaceutical and Nutraceutical classifications."""
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(120), unique=True, nullable=False, index=True)
    type = db.Column(db.String(30), nullable=False, default='pharmaceutical')  # 'pharmaceutical' or 'nutraceutical'
    description = db.Column(db.Text, nullable=True)
    icon = db.Column(db.String(50), default='fa-capsules')
    display_order = db.Column(db.Integer, default=0)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=utcnow)
    
    products = db.relationship('Product', backref='category', lazy='dynamic', cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'slug': self.slug,
            'type': self.type,
            'description': self.description,
            'icon': self.icon,
            'product_count': self.products.filter_by(is_active=True).count()
        }
        
    def __repr__(self):
        return f'<Category {self.name} ({self.type})>'


class Product(db.Model):
    """Product model for pharmaceutical and nutraceutical portfolio."""
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False, index=True)
    slug = db.Column(db.String(220), unique=True, nullable=False, index=True)
    type = db.Column(db.String(30), nullable=False, default='pharmaceutical', index=True)  # 'pharmaceutical' or 'nutraceutical'
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False, index=True)
    
    composition = db.Column(db.Text, nullable=False)
    dosage_form = db.Column(db.String(100), nullable=False, index=True)  # Tablets, Capsules, Injections, Syrups, Powders, Softgels, etc.
    strength = db.Column(db.String(100), nullable=True)
    packaging = db.Column(db.String(150), nullable=True)
    description = db.Column(db.Text, nullable=True)
    indications = db.Column(db.String(255), nullable=True)  # Therapeutic Segment or General Category
    
    available_markets = db.Column(db.String(255), default='Asia, Africa, Middle East, CIS, Latin America')
    dossier_status = db.Column(db.String(100), default='CTD / ACTD Dossier Available on Request')
    stability_status = db.Column(db.String(100), default='Zone IVb Real-Time & Accelerated Data Available')
    validation_status = db.Column(db.String(100), default='Validated Process & Analytical Methods')
    coa_status = db.Column(db.String(100), default='Certificate of Analysis Provided with Each Batch')
    
    image_url = db.Column(db.String(255), nullable=True)
    is_featured = db.Column(db.Boolean, default=False, index=True)
    is_active = db.Column(db.Boolean, default=True, index=True)
    
    created_at = db.Column(db.DateTime, default=utcnow)
    updated_at = db.Column(db.DateTime, default=utcnow, onupdate=utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'slug': self.slug,
            'type': self.type,
            'category_id': self.category_id,
            'category_name': self.category.name if self.category else '',
            'category_slug': self.category.slug if self.category else '',
            'composition': self.composition,
            'dosage_form': self.dosage_form,
            'strength': self.strength or '',
            'packaging': self.packaging or '',
            'description': self.description or '',
            'indications': self.indications or '',
            'available_markets': self.available_markets or '',
            'dossier_status': self.dossier_status or '',
            'stability_status': self.stability_status or '',
            'validation_status': self.validation_status or '',
            'coa_status': self.coa_status or '',
            'image_url': self.image_url or '',
            'is_featured': self.is_featured,
            'is_active': self.is_active,
            'created_at': self.created_at.strftime('%Y-%m-%d') if self.created_at else ''
        }
        
    def __repr__(self):
        return f'<Product {self.name}>'


class Enquiry(db.Model):
    """Enquiry model for B2B business inquiries, contact submissions, and product requests."""
    __tablename__ = 'enquiries'
    
    id = db.Column(db.Integer, primary_key=True)
    enquiry_type = db.Column(db.String(50), default='business_partnership')  # 'business_partnership', 'general_contact', 'product_inquiry'
    
    full_name = db.Column(db.String(120), nullable=False)
    company_name = db.Column(db.String(150), nullable=True)
    business_type = db.Column(db.String(80), nullable=True)  # Distributor, Importer, Wholesaler, Pharmaceutical Company, Healthcare Company, Other
    email = db.Column(db.String(120), nullable=False, index=True)
    phone = db.Column(db.String(50), nullable=True)
    country = db.Column(db.String(100), nullable=True)
    
    product_name = db.Column(db.String(200), nullable=True)
    category = db.Column(db.String(100), nullable=True)
    subject = db.Column(db.String(200), nullable=True)
    message = db.Column(db.Text, nullable=False)
    
    file_attachment = db.Column(db.String(255), nullable=True)
    status = db.Column(db.String(30), default='new', index=True)  # 'new', 'in_review', 'contacted', 'closed'
    admin_notes = db.Column(db.Text, nullable=True)
    ip_address = db.Column(db.String(50), nullable=True)
    
    created_at = db.Column(db.DateTime, default=utcnow, index=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'enquiry_type': self.enquiry_type,
            'full_name': self.full_name,
            'company_name': self.company_name or '',
            'business_type': self.business_type or '',
            'email': self.email,
            'phone': self.phone or '',
            'country': self.country or '',
            'product_name': self.product_name or '',
            'category': self.category or '',
            'subject': self.subject or '',
            'message': self.message,
            'file_attachment': self.file_attachment or '',
            'status': self.status,
            'admin_notes': self.admin_notes or '',
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M') if self.created_at else ''
        }
        
    def __repr__(self):
        return f'<Enquiry #{self.id} from {self.full_name} ({self.company_name})>'


class SiteSetting(db.Model):
    """Dynamic site configuration settings model for contact info and trust statistics."""
    __tablename__ = 'site_settings'
    
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(80), unique=True, nullable=False, index=True)
    value = db.Column(db.Text, nullable=True)
    description = db.Column(db.String(255), nullable=True)
    group = db.Column(db.String(50), default='general')  # 'contact', 'metrics', 'company', 'social'
    
    @classmethod
    def get_value(cls, key, default=''):
        """Retrieve setting value by key."""
        setting = cls.query.filter_by(key=key).first()
        return setting.value if setting and setting.value is not None else default

    @classmethod
    def set_value(cls, key, value, description=None, group='general'):
        """Update or insert a setting."""
        setting = cls.query.filter_by(key=key).first()
        if not setting:
            setting = cls(key=key, value=value, description=description, group=group)
            db.session.add(setting)
        else:
            setting.value = value
            if description:
                setting.description = description
            if group:
                setting.group = group
        db.session.commit()
        return setting
    
    def __repr__(self):
        return f'<SiteSetting {self.key}={self.value}>'
