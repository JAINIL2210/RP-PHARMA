# RP PHARMA — Corporate Website & B2B Portal

A professional, modern, interactive, and fully responsive corporate website and B2B portal for **RP PHARMA**, an Indian pharmaceutical and nutraceutical manufacturing, export, and healthcare company.

---

## 🌟 Key Features

1. **Brand & Corporate Presentation**
   - Headquartered in India with international reach across Asia, Africa, Middle East, CIS, and Latin America.
   - Strict adherence to pharmaceutical compliance, WHO-GMP partner standards, CTD/ACTD regulatory dossiers, and ICH Zone IVb stability testing data.
   - Dynamic placeholders for contact details (`[OFFICE ADDRESS]`, `[OFFICIAL PHONE]`, `[OFFICIAL EMAIL]`, etc.) and trust metrics.

2. **Interactive Product Catalogue**
   - Searchable & filterable catalogue by division (Pharmaceutical / Nutraceutical), therapeutic category, dosage form, and active molecule/composition.
   - Individual Product Detail pages with composition monographs, strength, packaging, stability & dossier status, and related products.
   - Instant "Enquire Now" modal pre-filling product details for seamless quote requests.

3. **B2B Partnership & Enquiry Workflows**
   - Specialized B2B partnership application form for international distributors, importers, and wholesalers.
   - Direct Contact Form with anti-spam security (Honeypot trap + math verification challenge).
   - Document attachment uploads (PDF, DOCX, JPG, PNG up to 10MB).
   - Floating WhatsApp direct chat widget pulling live numbers from website settings.

4. **Administration Portal (`/admin`)**
   - **Dashboard:** Key metrics (total products, pharma vs nutra split, total enquiries, pending leads).
   - **Product Manager:** Add, edit, delete formulations with image upload and technical specifications.
   - **Category Manager:** Manage therapeutic and wellness categories.
   - **Enquiry Manager:** Filter enquiries by status (`New`, `In Review`, `Contacted`, `Closed`), inspect submissions, download attachments, and export to CSV.
   - **Website Settings:** Dynamically update office addresses, contact numbers, email desks, WhatsApp numbers, trust counters, and social media channels without modifying code.

5. **SEO & Performance**
   - JSON-LD Structured Data for `Organization`, `MedicalBusiness`, and `Product`.
   - Dynamic XML Sitemap (`/sitemap.xml`) and `robots.txt`.
   - OpenGraph and Twitter card social meta tags.

---

## 🛠️ Technology Stack

- **Backend:** Python 3, Flask, Flask-SQLAlchemy, Werkzeug, Jinja2
- **Database:** SQLAlchemy ORM with automatic SQLite out-of-the-box local setup and one-line configuration for MySQL.
- **Frontend:** Semantic HTML5, CSS3 with custom HSL design tokens, Bootstrap 5.3, JavaScript (ES6+), Font Awesome 6.

---

## 🚀 Quick Start & Local Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Application
```bash
python run.py
```
The server will start at `http://127.0.0.1:5000` and automatically create and seed the database with initial categories, products, and default settings.

---

## 🔐 Admin Credentials

- **Admin URL:** `http://127.0.0.1:5000/admin`
- **Default Username:** `admin`
- **Default Password:** `Admin@RP2026`

*(Admin credentials and settings can be changed directly from the Admin Portal or `.env` configuration)*

---

## 🗄️ Database Configuration (MySQL Connection)

By default, the application runs on SQLite (`instance/rp_pharma.db`). To connect to a MySQL database:

1. Create a MySQL database:
   ```sql
   CREATE DATABASE rp_pharma_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```
2. Set the `DATABASE_URI` environment variable in `.env`:
   ```env
   DATABASE_URI=mysql+pymysql://username:password@localhost:3306/rp_pharma_db
   ```
3. Run `python run.py`. SQLAlchemy will automatically create all tables and seed the catalog into MySQL.

---

## 📡 REST API Endpoints

- `GET /api/products` — List filterable products (`?type=pharmaceutical&category=antibiotics&search=amoxicillin`)
- `GET /api/products/<id>` — Retrieve single product details
- `GET /api/categories` — List all active categories
- `GET /api/settings` — Get public company configuration

---

## 📁 Project Structure

```
RP PHARMA/
├── app/
│   ├── __init__.py          # Flask factory, context processor, error handlers
│   ├── config.py            # App configurations (Development, Production)
│   ├── models.py            # SQLAlchemy models: Product, Category, Enquiry, SiteSetting, AdminUser
│   ├── seed_data.py         # Initial database seeder
│   ├── routes/
│   │   ├── main.py          # Public routes (Home, About, Quality, Manufacturing, Global, Contact)
│   │   ├── products.py      # Pharmaceuticals, Nutraceuticals, Catalogue, Product Detail
│   │   ├── enquiries.py     # Form submissions & file upload handlers
│   │   ├── admin.py         # Admin dashboard, CRUD, enquiries & settings
│   │   └── api.py           # REST APIs
│   ├── static/
│   │   ├── css/
│   │   │   ├── style.css    # Master pharmaceutical design system
│   │   │   └── admin.css    # Admin portal styles
│   │   ├── js/
│   │   │   ├── main.js      # Sticky navbar, animated counters, modals
│   │   │   ├── products.js  # Live catalogue search & multi-facet filters
│   │   │   ├── map.js       # Interactive world map regions
│   │   │   └── admin.js     # Admin interactions & confirmations
│   │   └── uploads/         # Enquiries attachments & product images
│   └── templates/           # Jinja2 HTML templates
├── instance/                # SQLite database folder
├── requirements.txt         # Dependencies
├── run.py                   # Application runner
└── README.md                # Documentation
```

---

## 📄 License & Copyright

&copy; 2026 RP PHARMA. All Rights Reserved.
