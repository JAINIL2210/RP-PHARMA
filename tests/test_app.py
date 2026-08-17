import unittest
import json
from app import create_app
from app.models import db, Product, Category, Enquiry, SiteSetting, AdminUser
from app.seed_data import seed_database

class RPPharmaTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('development')
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()
            seed_database()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_database_seeded(self):
        """Verify that products, categories, settings and admin user are seeded."""
        with self.app.app_context():
            self.assertGreater(Product.query.count(), 0)
            self.assertGreater(Category.query.count(), 0)
            self.assertIsNotNone(SiteSetting.get_value('office_address'))
            admin = AdminUser.query.filter_by(username='admin').first()
            self.assertIsNotNone(admin)
            self.assertTrue(admin.check_password('Admin@RP2026'))

    def test_public_pages_status_codes(self):
        """Verify all main public pages render with HTTP 200."""
        routes = [
            '/',
            '/about',
            '/pharmaceuticals',
            '/nutraceuticals',
            '/products',
            '/quality',
            '/manufacturing',
            '/global-presence',
            '/business-enquiry',
            '/contact',
            '/privacy-policy',
            '/terms',
            '/sitemap.xml',
            '/robots.txt'
        ]
        for route in routes:
            response = self.client.get(route)
            self.assertEqual(response.status_code, 200, f"Route {route} failed with status {response.status_code}")

    def test_product_detail_page(self):
        """Verify individual product detail page loads."""
        with self.app.app_context():
            prod = Product.query.first()
            self.assertIsNotNone(prod)
            slug = prod.slug
            
        response = self.client.get(f'/product/{slug}')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Product Specifications', response.data)

    def test_enquiry_submission(self):
        """Verify business enquiry form submission."""
        response = self.client.post('/enquiry/submit', data={
            'enquiry_type': 'business_partnership',
            'full_name': 'Test Importer',
            'company_name': 'Global Meds Ltd',
            'business_type': 'Importer',
            'email': 'importer@testmeds.com',
            'phone': '+1234567890',
            'country': 'Vietnam',
            'product_name': 'Amoxicillin & Potassium Clavulanate Tablets',
            'category': 'Antibiotics & Anti-Infectives',
            'message': 'We require 50,000 packs with CTD dossier for local health registration.',
            'captcha_answer': '7',
            'captcha_expected': '7',
            'website_hp': ''
        }, follow_redirects=True)
        
        self.assertEqual(response.status_code, 200)
        with self.app.app_context():
            enq = Enquiry.query.filter_by(email='importer@testmeds.com').first()
            self.assertIsNotNone(enq)
            self.assertEqual(enq.full_name, 'Test Importer')
            self.assertEqual(enq.status, 'new')

    def test_honeypot_spam_blocking(self):
        """Verify honeypot blocks automated bot submissions."""
        response = self.client.post('/enquiry/submit', data={
            'full_name': 'Bot User',
            'email': 'bot@spam.com',
            'message': 'Buy cheap crypto',
            'website_hp': 'http://spam-link.com'
        }, follow_redirects=True)
        
        with self.app.app_context():
            enq = Enquiry.query.filter_by(email='bot@spam.com').first()
            self.assertIsNone(enq)

    def test_api_products(self):
        """Verify REST API returns valid JSON product list."""
        response = self.client.get('/api/products?type=pharmaceutical')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data['success'])
        self.assertGreater(data['count'], 0)

    def test_admin_authentication_and_dashboard(self):
        """Verify admin login and access to dashboard."""
        # Unauthenticated access should redirect to login
        res_unauth = self.client.get('/admin/dashboard')
        self.assertEqual(res_unauth.status_code, 302)

        # Login with correct credentials
        res_login = self.client.post('/admin/login', data={
            'username': 'admin',
            'password': 'Admin@RP2026'
        }, follow_redirects=True)
        self.assertEqual(res_login.status_code, 200)
        self.assertIn(b'Dashboard Overview', res_login.data)

        # Test settings update
        res_settings = self.client.post('/admin/settings', data={
            'stat_experience': '20+'
        }, follow_redirects=True)
        self.assertEqual(res_settings.status_code, 200)

        with self.app.app_context():
            val = SiteSetting.get_value('stat_experience')
            self.assertEqual(val, '20+')

if __name__ == '__main__':
    unittest.main()
