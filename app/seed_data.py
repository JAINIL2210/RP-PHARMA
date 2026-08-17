from app.models import db, AdminUser, Category, Product, SiteSetting, slugify

def seed_database():
    """Seed initial data for RP PHARMA."""
    
    # 1. Seed Site Settings (with official placeholders from prompt)
    default_settings = [
        # Company Info
        ('company_name', 'RP PHARMA', 'Official Company Name', 'company'),
        ('tagline', 'Your Trusted Partner in Pharmaceuticals & Nutraceuticals', 'Brand Tagline', 'company'),
        ('company_intro', (
            'RP PHARMA is a global pharmaceutical company headquartered in India, with proven expertise '
            'in the pharmaceutical industry. We bring together deep knowledge in technical, regulatory and '
            'international marketing to deliver high-quality healthcare solutions across global markets. '
            'Our formulations are manufactured in state-of-the-art facilities across India, following '
            'applicable WHO-GMP and EU-GMP standards and requirements. Products are supported by comprehensive '
            'technical documentation, including dossiers, stability studies and validation data, reinforcing '
            'our commitment to transparency and regulatory compliance.'
        ), 'Company Profile Introduction', 'company'),
        ('vision', 'To become a trusted global partner for pharmaceutical and nutraceutical solutions.', 'Company Vision Statement', 'company'),
        ('mission', 'To deliver quality-focused, compliant and reliable healthcare products while building long-term relationships with customers and partners.', 'Company Mission Statement', 'company'),
        
        # Contact Information (Placeholders as specified in prompt)
        ('office_address', '[Complete Corporate Office Address], [City, State, PIN Code], India', 'Registered / Corporate Office Address', 'contact'),
        ('official_email', '[Official Email Address]', 'General Official Email', 'contact'),
        ('official_phone', '[Official Phone Number]', 'Official Phone Number', 'contact'),
        ('whatsapp_number', '[Official WhatsApp Number]', 'Official WhatsApp Business Number (e.g. +91 98765 43210)', 'contact'),
        ('whatsapp_raw_number', '919876543210', 'Raw WhatsApp Number for wa.me links (digits only)', 'contact'),
        ('business_email', '[Business Email]', 'Business Enquiries Email', 'contact'),
        ('export_email', '[Export Email]', 'Export Enquiries Email', 'contact'),
        ('working_hours', 'Monday – Saturday: 9:00 AM – 6:00 PM (IST)', 'Office Working Hours', 'contact'),
        ('google_maps_embed', '', 'Google Maps Embed URL / Iframe src', 'contact'),
        
        # Trust Statistics (Placeholders clearly marked)
        ('stat_experience', '15+', 'Years of Industry Leadership Placeholder', 'metrics'),
        ('stat_countries', '25+', 'Countries Served Across Emerging Markets', 'metrics'),
        ('stat_categories', '10+', 'Therapeutic & Wellness Categories', 'metrics'),
        ('stat_manufacturing_partners', '10+', 'Qualified Manufacturing Partner Facilities in India', 'metrics'),
        ('stat_global_markets', '5', 'Global Continental Regions (Asia, Africa, Middle East, CIS, LATAM)', 'metrics'),
        ('stat_formulations', '150+', 'Formulations & SKUs Portfolio', 'metrics'),
        
        # Social links (Placeholders)
        ('linkedin_url', '', 'LinkedIn Corporate Page URL', 'social'),
        ('twitter_url', '', 'Twitter / X Profile URL', 'social'),
        ('facebook_url', '', 'Facebook Page URL', 'social'),
    ]
    
    for key, val, desc, grp in default_settings:
        if not SiteSetting.query.filter_by(key=key).first():
            setting = SiteSetting(key=key, value=val, description=desc, group=grp)
            db.session.add(setting)
            
    # 2. Seed Default Admin User
    if not AdminUser.query.filter_by(username='admin').first():
        admin = AdminUser(
            username='admin',
            email='admin@rppharma.com',
            role='superadmin',
            is_active=True
        )
        admin.set_password('Admin@RP2026')
        db.session.add(admin)
        print("[+] Admin user created: admin / Admin@RP2026")

    # 3. Seed Categories
    pharma_categories = [
        ('Antibiotics & Anti-Infectives', 'Broad-spectrum anti-bacterial and anti-infective formulations.', 'fa-shield-virus', 1),
        ('Cardiovascular', 'Formulations for hypertension, cardiovascular management, and lipid care.', 'fa-heart-pulse', 2),
        ('Gastrointestinal', 'Formulations for acid peptic disorders, GI motility, and digestive health.', 'fa-pills', 3),
        ('Anti-diabetic', 'Oral hypoglycemic agents and metabolic health formulations.', 'fa-dna', 4),
        ('Pain Management & Analgesics', 'Non-steroidal anti-inflammatory drugs (NSAIDs) and analgesic formulations.', 'fa-hand-holding-medical', 5),
        ('Vitamins & Minerals (Pharma)', 'Therapeutic grade vitamins, minerals, and hematinics.', 'fa-flask', 6),
        ('Specialty Formulations', 'Targeted formulations across specialty therapeutic segments.', 'fa-microscope', 7),
        ('Respiratory & Anti-Allergic', 'Formulations for respiratory care, bronchodilation, and anti-allergic support.', 'fa-lungs', 8),
    ]
    
    nutra_categories = [
        ('Vitamins & Multivitamins', 'Comprehensive daily vitamin formulations for wellness and vitality.', 'fa-sun', 1),
        ('Essential Minerals & Calcium', 'Targeted mineral supplements, bone health, and electrolyte balance.', 'fa-bone', 2),
        ('Nutritional & Protein Supplements', 'Advanced dietary nutrition, amino acids, and protein blends.', 'fa-dumbbell', 3),
        ('General Wellness & Immunity', 'Daily wellness, antioxidant complex, and immune defense supplements.', 'fa-leaf', 4),
        ('Specialty Nutrition', 'Targeted nutrition for joint health, cognitive focus, and cardiovascular wellness.', 'fa-brain', 5),
        ('Herbal & Botanical Extracts', 'Standardized herbal and botanical wellness supplements.', 'fa-seedling', 6),
    ]
    
    cat_map = {}
    
    for name, desc, icon, order in pharma_categories:
        slug = slugify(name)
        cat = Category.query.filter_by(slug=slug).first()
        if not cat:
            cat = Category(
                name=name,
                slug=slug,
                type='pharmaceutical',
                description=desc,
                icon=icon,
                display_order=order,
                is_active=True
            )
            db.session.add(cat)
            db.session.flush()
        cat_map[name] = cat.id
        
    for name, desc, icon, order in nutra_categories:
        slug = slugify(name)
        cat = Category.query.filter_by(slug=slug).first()
        if not cat:
            cat = Category(
                name=name,
                slug=slug,
                type='nutraceutical',
                description=desc,
                icon=icon,
                display_order=order,
                is_active=True
            )
            db.session.add(cat)
            db.session.flush()
        cat_map[name] = cat.id
        
    db.session.commit()
    
    # 4. Seed Products
    products_data = [
        # --- PHARMACEUTICALS ---
        {
            'name': 'Amoxicillin & Potassium Clavulanate Tablets',
            'type': 'pharmaceutical',
            'category_name': 'Antibiotics & Anti-Infectives',
            'composition': 'Amoxicillin Trihydrate IP eq. to Amoxicillin 500 mg + Potassium Clavulanate Diluted IP eq. to Clavulanic Acid 125 mg',
            'dosage_form': 'Film-Coated Tablets',
            'strength': '625 mg (500mg + 125mg)',
            'packaging': '10 x 1 x 6 Alu-Alu Blister Pack / 10 x 10 Blister',
            'description': 'High quality broad-spectrum antibacterial formulation manufactured in compliance with WHO-GMP standards for respiratory, skin, and urinary tract bacterial infections.',
            'indications': 'Bacterial Infections / Anti-Infective',
            'available_markets': 'Asia, Africa, Middle East, CIS, Latin America',
            'dossier_status': 'CTD / ACTD Dossier Available',
            'stability_status': 'Zone IVb Real-Time & Accelerated Stability Data Available',
            'validation_status': 'Complete Process & Analytical Validation Reports',
            'is_featured': True,
        },
        {
            'name': 'Azithromycin Tablets',
            'type': 'pharmaceutical',
            'category_name': 'Antibiotics & Anti-Infectives',
            'composition': 'Azithromycin Dihydrate IP eq. to Anhydrous Azithromycin 500 mg',
            'dosage_form': 'Film-Coated Tablets',
            'strength': '500 mg / 250 mg',
            'packaging': '1 x 3 Tablets Blister / 10 x 3 Alu-Alu Pack',
            'description': 'Macrolide antibiotic formulation indicated for upper and lower respiratory tract infections, skin infections, and genital tract infections.',
            'indications': 'Macrolide Antibiotic / Respiratory Infections',
            'available_markets': 'Global Export Markets',
            'dossier_status': 'CTD Format Dossier Available',
            'stability_status': 'Zone IVb Stability Tested',
            'validation_status': 'Process Validation Completed',
            'is_featured': True,
        },
        {
            'name': 'Cefixime Tablets',
            'type': 'pharmaceutical',
            'category_name': 'Antibiotics & Anti-Infectives',
            'composition': 'Cefixime Trihydrate IP eq. to Anhydrous Cefixime 200 mg',
            'dosage_form': 'Dispersible / Film-Coated Tablets',
            'strength': '200 mg / 400 mg',
            'packaging': '10 x 10 Alu-Alu Blister',
            'description': 'Third-generation cephalosporin antibiotic with broad spectrum against Gram-positive and Gram-negative pathogens.',
            'indications': 'Cephalosporin Antibiotic / Systemic Infections',
            'available_markets': 'Asia, Africa, Middle East',
            'dossier_status': 'CTD / ACTD Dossier Available',
            'stability_status': 'Zone IVb 36-Month Stability Data',
            'validation_status': 'Validated Analytical & Production Process',
            'is_featured': False,
        },
        {
            'name': 'Telmisartan & Amlodipine Tablets',
            'type': 'pharmaceutical',
            'category_name': 'Cardiovascular',
            'composition': 'Telmisartan IP 40 mg + Amlodipine Besylate IP eq. to Amlodipine 5 mg',
            'dosage_form': 'Bilayered Tablets',
            'strength': '40 mg + 5 mg / 80 mg + 5 mg',
            'packaging': '10 x 10 Alu-Alu Blister Pack in Monocarton',
            'description': 'Fixed-dose combination anti-hypertensive formulation combining an Angiotensin II receptor antagonist with a calcium channel blocker for blood pressure regulation.',
            'indications': 'Essential Hypertension / Cardiovascular Care',
            'available_markets': 'Asia, Africa, CIS, Latin America',
            'dossier_status': 'CTD Dossier (Module 1 to 5) Available',
            'stability_status': 'Zone IVb Stability Tested',
            'validation_status': 'Complete Validation Documentation',
            'is_featured': True,
        },
        {
            'name': 'Atorvastatin Tablets',
            'type': 'pharmaceutical',
            'category_name': 'Cardiovascular',
            'composition': 'Atorvastatin Calcium IP eq. to Atorvastatin 20 mg',
            'dosage_form': 'Film-Coated Tablets',
            'strength': '10 mg / 20 mg / 40 mg',
            'packaging': '10 x 10 Alu-Alu Blister Pack',
            'description': 'HMG-CoA reductase inhibitor lipid-lowering agent indicated for hypercholesterolemia and cardiovascular risk reduction.',
            'indications': 'Lipid Lowering / Cardiovascular Health',
            'available_markets': 'Global Export Markets',
            'dossier_status': 'CTD Dossier Available',
            'stability_status': 'Zone IVb Stability Available',
            'validation_status': 'Process Validation Completed',
            'is_featured': False,
        },
        {
            'name': 'Pantoprazole Gastro-Resistant Tablets',
            'type': 'pharmaceutical',
            'category_name': 'Gastrointestinal',
            'composition': 'Pantoprazole Sodium Sesquihydrate IP eq. to Pantoprazole 40 mg',
            'dosage_form': 'Enteric-Coated Tablets',
            'strength': '40 mg',
            'packaging': '10 x 10 Alu-Alu Blister Pack',
            'description': 'Proton pump inhibitor formulated with enteric polymer coating to inhibit gastric acid secretion in GERD and peptic ulcer conditions.',
            'indications': 'Acid Peptic Disorders / Gastric Protection',
            'available_markets': 'Asia, Africa, Middle East, CIS, Latin America',
            'dossier_status': 'CTD Dossier Ready for Submission',
            'stability_status': 'Zone IVb Stability Data Available',
            'validation_status': 'Validated Manufacturing Process',
            'is_featured': True,
        },
        {
            'name': 'Omeprazole & Domperidone Capsules',
            'type': 'pharmaceutical',
            'category_name': 'Gastrointestinal',
            'composition': 'Omeprazole IP 20 mg (as enteric-coated pellets) + Domperidone IP 30 mg (as sustained-release pellets)',
            'dosage_form': 'Hard Gelatin Pellet Capsules',
            'strength': '20 mg + 30 mg (SR)',
            'packaging': '10 x 10 Alu-Alu Blister Pack',
            'description': 'Dual action gastroprokinetic and acid suppressant formulation for gastroesophageal reflux disease associated with nausea and dyspepsia.',
            'indications': 'GERD & Dyspepsia / Gastrointestinal Care',
            'available_markets': 'Global B2B Markets',
            'dossier_status': 'ACTD / CTD Dossier Available',
            'stability_status': 'Zone IVb Stability Data',
            'validation_status': 'Complete Validation Reports',
            'is_featured': False,
        },
        {
            'name': 'Metformin Hydrochloride Prolonged-Release Tablets',
            'type': 'pharmaceutical',
            'category_name': 'Anti-diabetic',
            'composition': 'Metformin Hydrochloride IP 500 mg (Prolonged-Release)',
            'dosage_form': 'Prolonged-Release Tablets',
            'strength': '500 mg / 800 mg / 1000 mg',
            'packaging': '10 x 10 Blister Pack / 1000 Tablets HDPE Container',
            'description': 'Biguanide oral antidiabetic prolonged-release matrix formulation designed for glycemic control in Type 2 diabetes mellitus.',
            'indications': 'Type 2 Diabetes Mellitus / Glycemic Control',
            'available_markets': 'Asia, Africa, CIS, Latin America',
            'dossier_status': 'CTD Dossier Available',
            'stability_status': 'Zone IVb Stability Data Available',
            'validation_status': 'Process Validation Complete',
            'is_featured': True,
        },
        {
            'name': 'Glimepiride & Metformin Tablets',
            'type': 'pharmaceutical',
            'category_name': 'Anti-diabetic',
            'composition': 'Glimepiride IP 2 mg + Metformin Hydrochloride IP 500 mg (Sustained-Release)',
            'dosage_form': 'Bilayered Tablets',
            'strength': '1mg+500mg / 2mg+500mg',
            'packaging': '10 x 10 Alu-Alu Blister',
            'description': 'Combination oral anti-hyperglycemic formulation for comprehensive glycemic management in adult patients.',
            'indications': 'Type 2 Diabetes / Metabolic Disorders',
            'available_markets': 'Global B2B Markets',
            'dossier_status': 'CTD Dossier on Request',
            'stability_status': 'Zone IVb Stability Tested',
            'validation_status': 'Validated Analytical Methods',
            'is_featured': False,
        },
        {
            'name': 'Paracetamol & Tramadol Hydrochloride Tablets',
            'type': 'pharmaceutical',
            'category_name': 'Pain Management & Analgesics',
            'composition': 'Tramadol Hydrochloride IP 37.5 mg + Paracetamol IP 325 mg',
            'dosage_form': 'Film-Coated Tablets',
            'strength': '37.5 mg + 325 mg',
            'packaging': '10 x 10 Alu-Alu Blister Pack',
            'description': 'Synergistic centrally acting analgesic and antipyretic fixed-dose combination for moderate to severe pain management.',
            'indications': 'Moderate to Severe Pain Management / Analgesia',
            'available_markets': 'Subject to Regulatory Import Approvals',
            'dossier_status': 'CTD Dossier Available',
            'stability_status': 'Zone IVb Stability Data',
            'validation_status': 'Process & Cleaning Validation Complete',
            'is_featured': False,
        },
        {
            'name': 'Aceclofenac, Paracetamol & Serratiopeptidase Tablets',
            'type': 'pharmaceutical',
            'category_name': 'Pain Management & Analgesics',
            'composition': 'Aceclofenac IP 100 mg + Paracetamol IP 325 mg + Serratiopeptidase IP 15 mg (as enteric coated granules)',
            'dosage_form': 'Film-Coated Tablets',
            'strength': '100 mg + 325 mg + 15 mg',
            'packaging': '10 x 10 Alu-Alu Blister Pack',
            'description': 'Triple combination anti-inflammatory, analgesic, and proteolytic enzyme formulation for acute musculoskeletal pain and edema reduction.',
            'indications': 'Musculoskeletal Pain & Post-Operative Inflammation',
            'available_markets': 'Asia, Africa, Latin America',
            'dossier_status': 'CTD / ACTD Dossier Available',
            'stability_status': 'Zone IVb Stability Tested',
            'validation_status': 'Complete Validation Documentation',
            'is_featured': True,
        },
        {
            'name': 'Montelukast Sodium & Levocetirizine Tablets',
            'type': 'pharmaceutical',
            'category_name': 'Respiratory & Anti-Allergic',
            'composition': 'Montelukast Sodium IP eq. to Montelukast 10 mg + Levocetirizine Dihydrochloride IP 5 mg',
            'dosage_form': 'Film-Coated Tablets',
            'strength': '10 mg + 5 mg',
            'packaging': '10 x 10 Alu-Alu Blister Pack',
            'description': 'Dual-action leukotriene receptor antagonist and selective H1-antihistaminic combination for seasonal and perennial allergic rhinitis.',
            'indications': 'Allergic Rhinitis & Bronchial Asthma Support',
            'available_markets': 'Asia, Africa, Middle East, CIS, Latin America',
            'dossier_status': 'CTD Dossier Available',
            'stability_status': 'Zone IVb Stability Tested',
            'validation_status': 'Process Validation Complete',
            'is_featured': False,
        },
        
        # --- NUTRACEUTICALS ---
        {
            'name': 'Multivitamin & Multi-Mineral Softgel Capsules',
            'type': 'nutraceutical',
            'category_name': 'Vitamins & Multivitamins',
            'composition': 'Vitamin A, Vitamin B-Complex (B1, B2, B6, B12, Niacinamide, Folic Acid), Vitamin C, Vitamin D3, Vitamin E, Zinc, Iron, Magnesium, Selenium & Iodine',
            'dosage_form': 'Soft Gelatin Capsules',
            'strength': 'Comprehensive Daily Formula',
            'packaging': '3 x 10 Blister / 60 Softgels HDPE Bottle',
            'description': 'Scientifically balanced daily multivitamin and essential mineral complex formulated in bioavailable softgel form to support everyday vitality, metabolic energy, and overall health.',
            'indications': 'Daily Nutritional Support / Micronutrient Balance',
            'available_markets': 'Global Export Markets',
            'dossier_status': 'Technical Dossier & Certificate of Free Sale Available',
            'stability_status': 'Real-Time & Accelerated Stability Data Available',
            'validation_status': 'GMP Compliant Facility Batch Testing',
            'is_featured': True,
        },
        {
            'name': 'Calcium Citrate Malate, Vitamin D3 & Magnesium Tablets',
            'type': 'nutraceutical',
            'category_name': 'Essential Minerals & Calcium',
            'composition': 'Calcium Citrate Malate eq. to Elemental Calcium 250 mg + Vitamin D3 400 IU + Magnesium Hydroxide eq. to Elemental Magnesium 100 mg + Zinc Sulphate 4 mg',
            'dosage_form': 'Film-Coated Tablets',
            'strength': 'Elemental Calcium 250mg + D3 400IU',
            'packaging': '10 x 15 Blister / 60 Tablets Bottle',
            'description': 'Highly bioavailable calcium citrate malate formulation fortified with Vitamin D3 and cofactor minerals to support bone mineral density, neuromuscular health, and skeletal strength.',
            'indications': 'Bone Mineral Density & Skeletal Support',
            'available_markets': 'Asia, Africa, Middle East, CIS, Latin America',
            'dossier_status': 'Complete Technical Specification Sheet & COA',
            'stability_status': '24-Month Stability Data Available',
            'validation_status': 'Standardized QC Analytical Parameters',
            'is_featured': True,
        },
        {
            'name': 'Omega-3 Fish Oil (1000mg) Softgel Capsules',
            'type': 'nutraceutical',
            'category_name': 'General Wellness & Immunity',
            'composition': 'Purified Deep Sea Fish Oil 1000 mg providing EPA (Eicosapentaenoic Acid) 180 mg + DHA (Docosahexaenoic Acid) 120 mg',
            'dosage_form': 'Enteric/Standard Softgel Capsules',
            'strength': '1000 mg (180 EPA / 120 DHA)',
            'packaging': '60 / 90 Softgels in Amber PET Container',
            'description': 'Molecularly distilled and heavy-metal tested essential fatty acid formulation rich in EPA and DHA to support cardiovascular wellness, joint flexibility, and cognitive vitality.',
            'indications': 'Cardiovascular Wellness & Cognitive Support',
            'available_markets': 'Global B2B Markets',
            'dossier_status': 'Technical Specification & Analytical Monograph Available',
            'stability_status': 'Zone IVb Stability Tested',
            'validation_status': 'Heavy Metal & Peroxide Value Tested',
            'is_featured': True,
        },
        {
            'name': 'Glucosamine, Chondroitin & MSM Complex',
            'type': 'nutraceutical',
            'category_name': 'Specialty Nutrition',
            'composition': 'Glucosamine Sulphate Potassium Chloride 750 mg + Chondroitin Sulphate 100 mg + Methylsulfonylmethane (MSM) 250 mg + Boswellia Serrata Extract 50 mg',
            'dosage_form': 'Film-Coated Tablets',
            'strength': 'Triple Joint Support Formula',
            'packaging': '60 Tablets in High Barrier Bottle',
            'description': 'Comprehensive structural joint care formulation designed to support cartilage synthesis, joint comfort, and mobility in active adults.',
            'indications': 'Joint Mobility & Cartilage Support',
            'available_markets': 'Global Export Markets',
            'dossier_status': 'Technical Dossier Available',
            'stability_status': 'Accelerated Stability Tested',
            'validation_status': 'Standardized Herbal & Chemical Assay',
            'is_featured': False,
        },
        {
            'name': 'Vitamin C & Zinc Chewable Tablets',
            'type': 'nutraceutical',
            'category_name': 'General Wellness & Immunity',
            'composition': 'Ascorbic Acid IP 100 mg + Sodium Ascorbate IP 450 mg (eq. to Total Vitamin C 500 mg) + Zinc Citrate eq. to Elemental Zinc 5 mg',
            'dosage_form': 'Orange Flavored Chewable Tablets',
            'strength': '500 mg Vitamin C + 5 mg Zinc',
            'packaging': '10 x 10 Blister / 30 Chewable Tablets Strip Pack',
            'description': 'Pleasantly flavored dual antioxidant chewable tablet formulation designed for immune system support and antioxidant defense against oxidative stress.',
            'indications': 'Immune Defense & Antioxidant Support',
            'available_markets': 'Asia, Africa, Middle East, CIS, Latin America',
            'dossier_status': 'Technical File Available',
            'stability_status': 'Zone IVb Stability Data Available',
            'validation_status': 'Standardized Flavor & Content Uniformity',
            'is_featured': True,
        },
        {
            'name': 'Coenzyme Q10 & L-Carnitine Capsules',
            'type': 'nutraceutical',
            'category_name': 'Specialty Nutrition',
            'composition': 'Coenzyme Q10 (Ubidecarenone) 100 mg + L-Carnitine L-Tartrate 500 mg + Lycopene (10%) 5000 mcg + Vitamin E 25 IU',
            'dosage_form': 'Hard / Soft Gelatin Capsules',
            'strength': 'CoQ10 100 mg + L-Carnitine 500 mg',
            'packaging': '3 x 10 Blister in Monocarton',
            'description': 'Cellular energy and antioxidant supplement providing bioenergetic cofactors to support mitochondrial function and cardiovascular vitality.',
            'indications': 'Mitochondrial Energy & Cellular Antioxidant',
            'available_markets': 'Global Export Markets',
            'dossier_status': 'Technical Specifications & Certificate of Analysis',
            'stability_status': 'Stability Validated',
            'validation_status': 'Process Validation Complete',
            'is_featured': False,
        }
    ]
    
    for item in products_data:
        slug = slugify(item['name'])
        prod = Product.query.filter_by(slug=slug).first()
        if not prod:
            cat_id = cat_map.get(item['category_name'])
            if cat_id:
                prod = Product(
                    name=item['name'],
                    slug=slug,
                    type=item['type'],
                    category_id=cat_id,
                    composition=item['composition'],
                    dosage_form=item['dosage_form'],
                    strength=item['strength'],
                    packaging=item['packaging'],
                    description=item['description'],
                    indications=item['indications'],
                    available_markets=item['available_markets'],
                    dossier_status=item['dossier_status'],
                    stability_status=item['stability_status'],
                    validation_status=item['validation_status'],
                    is_featured=item.get('is_featured', False),
                    is_active=True
                )
                db.session.add(prod)
                
    db.session.commit()
    print("[+] Database successfully seeded with RP PHARMA categories, products, settings, and admin user.")
