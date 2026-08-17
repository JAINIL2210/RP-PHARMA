# RP PHARMA — Corporate Website

A professional, modern, interactive, and fully responsive corporate website for **RP PHARMA**, an Indian pharmaceutical and nutraceutical manufacturing and export company.

---

## 🌟 Tech Stack

- **HTML5 & Vanilla CSS3** (Custom Modern Medical Blue & Cyan Design System)
- **PHP 7.4+ / PHP 8.x** (Modular pages, data layer & form processors)
- **JSON** (Lightning-fast embedded data storage: products, categories, site settings)
- **SQL (MySQL / MariaDB)** (`sql/schema.sql` table schema and seed data)
- **JavaScript (ES6+)** (Dynamic client-side product filtering, animated counters, region maps)
- **Bootstrap 5.3.3 & FontAwesome 6.5**

---

## 📁 Project Structure

```text
RP-PHARMA/
│
├── index.php                 # Home page (Hero, Stats, Formulations, Quality, Ecosystem, FAQ)
├── about.php                 # Corporate profile, Vision, Mission, Core Values
├── pharmaceuticals.php       # Finished pharmaceutical dosage forms & therapeutic segments
├── nutraceuticals.php        # Nutritional supplements & delivery formats
├── products.php              # Live searchable & filterable product catalogue
├── product-detail.php        # Comprehensive product detail page (?slug=...)
├── quality.php               # Quality assurance, CTD dossiers, Zone IVb stability
├── manufacturing.php         # 7-Step manufacturing ecosystem & facilities
├── global-presence.php       # International markets & export focus
├── contact.php               # Contact Us (+91 84690 34869, WhatsApp, Inquiry Form)
├── privacy-policy.php        # Privacy Policy
├── terms.php                 # Terms & Conditions
│
├── includes/
│   ├── header.php            # Responsive navbar, topbar (+91 84690 34869), SEO meta
│   ├── footer.php            # Unified footer, floating WhatsApp, enquiry modal, scripts
│   ├── db.php                # PDO MySQL / SQLite connection + automatic JSON fallback
│   └── functions.php         # Data loaders, search/filtering, sanitization, anti-spam
│
├── data/
│   ├── products.json         # 18 pre-loaded finished formulations & specifications
│   ├── categories.json       # Pharmaceutical & nutraceutical therapeutic categories
│   └── settings.json         # Corporate info, phone (+91 84690 34869), emails, stats
│
├── sql/
│   └── schema.sql            # Complete MySQL / MariaDB table schema and seed data
│
├── api/
│   ├── products.php          # JSON REST API endpoint for real-time AJAX filtering
│   └── enquiry.php           # PHP enquiry form submission handler with honeypot security
│
└── assets/
    ├── css/
    │   └── style.css         # Modern Medical Blue (#0A3D62) & Cyan (#0077EE) stylesheet
    └── js/
        ├── main.js           # Animated stats, sticky navigation, back-to-top
        ├── products.js       # Live search & instant client-side category filters
        └── map.js            # Interactive continental region switcher
```

---

## 🚀 How to Run Locally

### Option 1: PHP Built-in Server
If you have PHP installed:
```bash
php -S 127.0.0.1:8000
```
Open **[http://127.0.0.1:8000](http://127.0.0.1:8000)** in your browser.

### Option 2: Apache / XAMPP / WAMP / cPanel
1. Copy all project files into your `htdocs` or `public_html` directory.
2. Open `http://localhost/RP-PHARMA/` in your browser.
3. *(Optional)* Import `sql/schema.sql` into your MySQL database using phpMyAdmin.

---

## 📞 Official Contact Integration
- **Direct Phone:** `+91 84690 34869`
- **Instant WhatsApp:** `+91 84690 34869` (`https://wa.me/918469034869`)
- **Official Email:** `info@rppharma.com` / `business@rppharma.com` / `export@rppharma.com`
