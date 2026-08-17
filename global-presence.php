<?php
/**
 * RP PHARMA — Global Presence & International Reach
 */
$page_title = 'Global Presence | RP PHARMA — From India to Global Markets';
$page_desc = 'Explore RP PHARMA\'s global export reach from India across Southeast Asia, Africa, Middle East, CIS, and Latin America. Become an international distributor.';

require_once __DIR__ . '/includes/header.php';
?>

<!-- Header Banner -->
<section class="py-5" style="background: linear-gradient(180deg, #F0F6FA 0%, #FFFFFF 100%); border-bottom:1px solid var(--border-color);">
  <div class="container py-3">
    <div class="row align-items-center">
      <div class="col-lg-8">
        <nav aria-label="breadcrumb">
          <ol class="breadcrumb small mb-2">
            <li class="breadcrumb-item"><a href="index.php">Home</a></li>
            <li class="breadcrumb-item active" aria-current="page">Global Presence</li>
          </ol>
        </nav>
        <span class="section-tag"><i class="fa-solid fa-earth-americas"></i> International Markets</span>
        <h1 class="display-6 fw-bold text-primary mb-2">From India to Global Markets</h1>
        <p class="lead text-body fs-6 mb-0">
          Connecting Indian pharmaceutical and nutraceutical manufacturing excellence with international distributors, healthcare systems, and institutional buyers worldwide.
        </p>
      </div>
    </div>
  </div>
</section>

<!-- Interactive Global Markets Section -->
<section class="py-5 bg-white">
  <div class="container py-2 py-md-4">
    
    <!-- Interactive Map Display Wrap -->
    <div class="map-container-wrap mb-5">
      <div class="row align-items-center g-4">
        <div class="col-lg-7">
          <div class="p-2 p-md-3">
            <span class="section-tag section-tag-light mb-3"><i class="fa-solid fa-location-crosshairs"></i> Regional Focus</span>
            <h3 class="text-white fw-bold mb-3" id="activeRegionName">Global Export Footprint</h3>
            <p class="text-white opacity-75 lead fs-6 mb-4" id="activeRegionDesc">
              Explore our continental export regions to review formulation availability, regulatory dossier support, and distributor collaboration.
            </p>

            <div class="d-flex flex-wrap gap-2 pt-2">
              <span class="badge bg-white bg-opacity-10 text-white border border-white border-opacity-20 px-3 py-2">
                <i class="fa-solid fa-plane-departure me-1"></i> Air Freight Support
              </span>
              <span class="badge bg-white bg-opacity-10 text-white border border-white border-opacity-20 px-3 py-2">
                <i class="fa-solid fa-ship me-1"></i> Ocean Freight
              </span>
              <span class="badge bg-white bg-opacity-10 text-white border border-white border-opacity-20 px-3 py-2">
                <i class="fa-solid fa-passport me-1"></i> Registration Support
              </span>
            </div>
          </div>
        </div>

        <div class="col-lg-5">
          <div class="p-4 bg-white bg-opacity-10 rounded-4 border border-white border-opacity-15 text-center">
            <div class="display-6 fw-bold text-white mb-2">India to World</div>
            <p class="text-white opacity-75 small mb-3">Headquartered in India with verified manufacturing partners</p>
            <a href="tel:<?= htmlspecialchars($site_settings['phone_digits'] ?? '918469034869') ?>" class="btn btn-rp-secondary w-100 mb-2">
              <i class="fa-solid fa-phone me-2"></i> Call <?= htmlspecialchars($site_settings['official_phone'] ?? '+91 84690 34869') ?>
            </a>
            <a href="contact.php" class="btn btn-rp-outline-white w-100">
              <i class="fa-solid fa-envelope me-2"></i> Send Market Inquiry
            </a>
          </div>
        </div>
      </div>
    </div>

    <!-- Regions Grid Cards -->
    <div class="row g-3 g-md-4 mb-5">
      <!-- Asia -->
      <div class="col-sm-6 col-lg-4">
        <div class="map-region-card h-100 bg-white border text-dark p-4 rounded-4 shadow-sm" data-region="asia">
          <div class="d-flex align-items-center justify-content-between mb-3">
            <h5 class="fw-bold text-primary mb-0"><i class="fa-solid fa-location-dot me-2" style="color:var(--accent);"></i> Southeast &amp; South Asia</h5>
            <span class="badge bg-primary text-white">Active</span>
          </div>
          <p class="small text-muted mb-3">
            Supplying anti-infective, cardiovascular, and pain management formulations supported by full ACTD/CTD regulatory dossiers.
          </p>
          <ul class="list-unstyled small text-muted mb-0">
            <li><i class="fa-solid fa-check text-primary me-1"></i> Zone IVb stability data</li>
            <li><i class="fa-solid fa-check text-primary me-1"></i> Customized multilingual packaging</li>
          </ul>
        </div>
      </div>

      <!-- Africa -->
      <div class="col-sm-6 col-lg-4">
        <div class="map-region-card h-100 bg-white border text-dark p-4 rounded-4 shadow-sm" data-region="africa">
          <div class="d-flex align-items-center justify-content-between mb-3">
            <h5 class="fw-bold text-primary mb-0"><i class="fa-solid fa-location-dot me-2" style="color:var(--accent);"></i> Africa</h5>
            <span class="badge bg-primary text-white">Key Region</span>
          </div>
          <p class="small text-muted mb-3">
            Partnering with private distributors, retail pharmacy chains, and institutional procurement agencies across Africa.
          </p>
          <ul class="list-unstyled small text-muted mb-0">
            <li><i class="fa-solid fa-check text-primary me-1"></i> Essential medicines &amp; antibiotics</li>
            <li><i class="fa-solid fa-check text-primary me-1"></i> Vitamins &amp; mineral supplements</li>
          </ul>
        </div>
      </div>

      <!-- Middle East -->
      <div class="col-sm-6 col-lg-4">
        <div class="map-region-card h-100 bg-white border text-dark p-4 rounded-4 shadow-sm" data-region="middle-east">
          <div class="d-flex align-items-center justify-content-between mb-3">
            <h5 class="fw-bold text-primary mb-0"><i class="fa-solid fa-location-dot me-2" style="color:var(--accent);"></i> Middle East &amp; GCC</h5>
            <span class="badge bg-primary text-white">Growing</span>
          </div>
          <p class="small text-muted mb-3">
            Focused on advanced nutraceutical wellness lines, premium softgel dietary supplements, and specialty therapeutic pharmaceuticals.
          </p>
          <ul class="list-unstyled small text-muted mb-0">
            <li><i class="fa-solid fa-check text-primary me-1"></i> Batch COA &amp; compliance data</li>
            <li><i class="fa-solid fa-check text-primary me-1"></i> High-barrier protective packaging</li>
          </ul>
        </div>
      </div>

      <!-- CIS -->
      <div class="col-sm-6 col-lg-4">
        <div class="map-region-card h-100 bg-white border text-dark p-4 rounded-4 shadow-sm" data-region="cis">
          <div class="d-flex align-items-center justify-content-between mb-3">
            <h5 class="fw-bold text-primary mb-0"><i class="fa-solid fa-location-dot me-2" style="color:var(--accent);"></i> CIS &amp; Central Asia</h5>
            <span class="badge bg-primary text-white">Expanding</span>
          </div>
          <p class="small text-muted mb-3">
            Dossier support aligned with regional drug regulatory requirements for cardiovascular and metabolic formulations.
          </p>
          <ul class="list-unstyled small text-muted mb-0">
            <li><i class="fa-solid fa-check text-primary me-1"></i> CTD dossier Module 1-5 ready</li>
            <li><i class="fa-solid fa-check text-primary me-1"></i> Validation study documentation</li>
          </ul>
        </div>
      </div>

      <!-- Latin America -->
      <div class="col-sm-6 col-lg-4">
        <div class="map-region-card h-100 bg-white border text-dark p-4 rounded-4 shadow-sm" data-region="latam">
          <div class="d-flex align-items-center justify-content-between mb-3">
            <h5 class="fw-bold text-primary mb-0"><i class="fa-solid fa-location-dot me-2" style="color:var(--accent);"></i> Latin America</h5>
            <span class="badge bg-primary text-white">Open</span>
          </div>
          <p class="small text-muted mb-3">
            Engaging pharmaceutical importers, distributor networks, and hospital supply tenders across Central and South American territories.
          </p>
          <ul class="list-unstyled small text-muted mb-0">
            <li><i class="fa-solid fa-check text-primary me-1"></i> Competitive export pricing</li>
            <li><i class="fa-solid fa-check text-primary me-1"></i> Standardized analytical testing</li>
          </ul>
        </div>
      </div>

      <!-- Global Opportunity -->
      <div class="col-sm-6 col-lg-4">
        <div class="map-region-card h-100 bg-light border text-dark p-4 rounded-4 shadow-sm" style="border-color: var(--accent) !important;">
          <div class="d-flex align-items-center justify-content-between mb-3">
            <h5 class="fw-bold text-primary mb-0"><i class="fa-solid fa-globe me-2" style="color:var(--accent);"></i> Other Global Markets</h5>
            <span class="badge bg-primary text-white">Open</span>
          </div>
          <p class="small text-muted mb-3">
            RP PHARMA welcomes international inquiries from licensed importers and healthcare enterprises worldwide.
          </p>
          <a href="contact.php" class="btn btn-sm btn-rp-outline w-100 mt-2">
            Submit Market Inquiry <i class="fa-solid fa-arrow-right ms-1"></i>
          </a>
        </div>
      </div>
    </div>

    <!-- Partnership Callout Section -->
    <div class="p-4 p-md-5 bg-light rounded-4 border text-center">
      <h3 class="fw-bold text-primary mb-2">Looking for a Pharmaceutical Partner in Your Market?</h3>
      <p class="lead text-muted fs-6 mb-4 mx-auto" style="max-width: 680px;">
        Join our growing international distributor network. We provide dedicated regulatory dossiers, competitive commercial pricing, and guaranteed supply consistency.
      </p>
      <div class="d-flex flex-column flex-sm-row justify-content-center gap-3">
        <a href="tel:<?= htmlspecialchars($site_settings['phone_digits'] ?? '918469034869') ?>" class="btn btn-rp-secondary">
          <i class="fa-solid fa-phone me-1"></i> Call <?= htmlspecialchars($site_settings['official_phone'] ?? '+91 84690 34869') ?>
        </a>
        <a href="products.php" class="btn btn-rp-outline">
          <i class="fa-solid fa-capsules me-1"></i> View Formulations
        </a>
      </div>
    </div>

  </div>
</section>

<?php
$extra_scripts = '<script src="assets/js/map.js"></script>';
require_once __DIR__ . '/includes/footer.php';
?>
