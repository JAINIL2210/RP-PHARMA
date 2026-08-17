<?php
/**
 * RP PHARMA — Product Catalogue Page
 */
$page_title = 'Product Catalogue | RP PHARMA — Pharmaceutical & Nutraceutical Portfolio';
$page_desc = 'Search and explore RP PHARMA\'s complete portfolio of pharmaceutical formulations and nutraceutical supplements manufactured in India for global export.';

require_once __DIR__ . '/includes/header.php';

$selected_type = isset($_GET['type']) ? trim($_GET['type']) : null;
$selected_category = isset($_GET['category']) ? trim($_GET['category']) : null;
$search_keyword = isset($_GET['search']) ? trim($_GET['search']) : null;

$pharma_categories = get_categories('pharmaceutical');
$nutra_categories = get_categories('nutraceutical');

$filters = [];
if ($selected_type && in_array($selected_type, ['pharmaceutical', 'nutraceutical'])) {
    $filters['type'] = $selected_type;
}
if ($selected_category) {
    $filters['category_slug'] = $selected_category;
}

$products = get_products($filters);
?>

<!-- Header Banner -->
<section class="py-5" style="background: linear-gradient(180deg, #F0F6FA 0%, #FFFFFF 100%); border-bottom:1px solid var(--border-color);">
  <div class="container py-3">
    <nav aria-label="breadcrumb">
      <ol class="breadcrumb small mb-2">
        <li class="breadcrumb-item"><a href="index.php">Home</a></li>
        <li class="breadcrumb-item active" aria-current="page">Product Catalogue</li>
      </ol>
    </nav>
    <div class="row align-items-center">
      <div class="col-lg-8">
        <span class="section-tag"><i class="fa-solid fa-boxes-stacked"></i> Complete Portfolio</span>
        <h1 class="display-6 fw-bold text-primary mb-2">Pharmaceutical &amp; Nutraceutical Catalogue</h1>
        <p class="lead text-body fs-6 mb-0">
          Search and filter our finished formulations, active compositions, and dietary supplements available for international B2B export and distribution.
        </p>
      </div>
    </div>
  </div>
</section>

<!-- Catalogue Search & Filters Main Section -->
<section class="py-5 bg-light">
  <div class="container">
    <div class="row g-4">
      
      <!-- Left Sidebar: Filters -->
      <div class="col-lg-3">
        <div class="p-3 p-md-4 bg-white rounded-3 border shadow-sm sticky-top" style="top: 80px; z-index: 10;">
          <div class="d-flex justify-content-between align-items-center mb-3 pb-2 border-bottom">
            <h5 class="fw-bold fs-6 text-primary mb-0"><i class="fa-solid fa-sliders me-2" style="color:var(--accent);"></i> Filter Products</h5>
            <button id="resetFiltersBtn" class="btn btn-sm btn-link text-decoration-none text-muted p-0" style="font-size:0.8rem;">
              <i class="fa-solid fa-rotate-left"></i> Reset
            </button>
          </div>

          <!-- Filter by Division / Type -->
          <div class="mb-4">
            <label class="form-label-custom d-block mb-2">Division</label>
            <div class="d-flex flex-column gap-2">
              <div class="form-check">
                <input class="form-check-input" type="radio" name="filterType" id="typeAll" value="all" <?= empty($selected_type) ? 'checked' : '' ?>>
                <label class="form-check-label small fw-semibold" for="typeAll">All Formulations</label>
              </div>
              <div class="form-check">
                <input class="form-check-input" type="radio" name="filterType" id="typePharma" value="pharmaceutical" <?= $selected_type === 'pharmaceutical' ? 'checked' : '' ?>>
                <label class="form-check-label small fw-semibold" for="typePharma">Pharmaceuticals</label>
              </div>
              <div class="form-check">
                <input class="form-check-input" type="radio" name="filterType" id="typeNutra" value="nutraceutical" <?= $selected_type === 'nutraceutical' ? 'checked' : '' ?>>
                <label class="form-check-label small fw-semibold" for="typeNutra">Nutraceuticals</label>
              </div>
            </div>
          </div>

          <!-- Filter by Category -->
          <div class="mb-4">
            <label class="form-label-custom d-block mb-2">Therapeutic / Wellness Category</label>
            <select class="form-select form-select-custom form-select-sm" id="filterCategorySelect">
              <option value="">All Categories</option>
              <optgroup label="Pharmaceuticals">
                <?php foreach ($pharma_categories as $cat): ?>
                <option value="<?= htmlspecialchars($cat['slug']) ?>" <?= $selected_category === $cat['slug'] ? 'selected' : '' ?>><?= htmlspecialchars($cat['name']) ?></option>
                <?php endforeach; ?>
              </optgroup>
              <optgroup label="Nutraceuticals">
                <?php foreach ($nutra_categories as $cat): ?>
                <option value="<?= htmlspecialchars($cat['slug']) ?>" <?= $selected_category === $cat['slug'] ? 'selected' : '' ?>><?= htmlspecialchars($cat['name']) ?></option>
                <?php endforeach; ?>
              </optgroup>
            </select>
          </div>

          <!-- Filter by Dosage Form -->
          <div class="mb-3">
            <label class="form-label-custom d-block mb-2">Dosage Form</label>
            <select class="form-select form-select-custom form-select-sm" id="filterDosageSelect">
              <option value="">All Dosage Forms</option>
              <option value="tablets">Tablets</option>
              <option value="capsules">Capsules</option>
              <option value="softgel">Softgels</option>
              <option value="syrup">Syrups / Liquid Orals</option>
              <option value="powder">Powders</option>
              <option value="effervescent">Effervescent</option>
            </select>
          </div>

          <div class="pt-3 border-top text-muted small">
            <i class="fa-solid fa-shield-halved me-1" style="color:var(--accent);"></i> Technical dossiers available for all formulations.
          </div>
        </div>
      </div>

      <!-- Right Column: Search Bar & Product Cards Grid -->
      <div class="col-lg-9">
        
        <!-- Search Input Bar -->
        <div class="p-3 bg-white rounded-3 border shadow-sm mb-4">
          <div class="row g-2 align-items-center">
            <div class="col-md-8">
              <div class="input-group">
                <span class="input-group-text bg-white border-end-0"><i class="fa-solid fa-magnifying-glass text-muted"></i></span>
                <input type="text" id="productSearchInput" class="form-control form-control-custom border-start-0" placeholder="Search by name, active molecule (e.g. Amoxicillin, Metformin, Omega-3)..." value="<?= htmlspecialchars($search_keyword ?? '') ?>">
              </div>
            </div>
            <div class="col-md-4 text-md-end text-muted small">
              Showing <span id="resultsCount" class="fw-bold text-primary"><?= count($products) ?></span> formulations
            </div>
          </div>
        </div>

        <!-- No Results Fallback -->
        <div id="noResultsMessage" class="p-5 text-center bg-white rounded-3 border" style="display:none;">
          <i class="fa-solid fa-box-open text-muted fs-1 mb-3"></i>
          <h4 class="fw-bold text-primary">No Matching Formulations Found</h4>
          <p class="text-muted small mb-3">Try adjusting your keyword search or resetting active filters.</p>
          <a href="contact.php" class="btn btn-sm btn-rp-secondary">
            Contact for Custom Requirements
          </a>
        </div>

        <!-- Product Grid -->
        <div class="row g-3 g-md-4" id="productsGrid">
          <?php foreach ($products as $prod): ?>
          <div class="col-sm-6 col-xl-4 product-grid-item"
               data-name="<?= htmlspecialchars($prod['name']) ?>"
               data-composition="<?= htmlspecialchars($prod['composition']) ?>"
               data-type="<?= htmlspecialchars($prod['type']) ?>"
               data-category="<?= htmlspecialchars($prod['category_slug'] ?? '') ?>"
               data-dosage="<?= htmlspecialchars($prod['dosage_form']) ?>"
               data-indications="<?= htmlspecialchars($prod['indications'] ?? '') ?>">
            <div class="product-card">
              <div class="product-card-header">
                <span class="product-type-badge <?= $prod['type'] === 'pharmaceutical' ? 'badge-pharma' : 'badge-nutra' ?>">
                  <?= ucfirst($prod['type']) ?>
                </span>
                <span class="small text-muted text-truncate ms-2" style="max-width: 130px;" title="<?= htmlspecialchars($prod['dosage_form']) ?>">
                  <i class="fa-solid fa-tablets me-1"></i><?= htmlspecialchars($prod['dosage_form']) ?>
                </span>
              </div>
              <div class="product-card-body">
                <h5 class="product-title"><?= htmlspecialchars($prod['name']) ?></h5>
                <div class="product-composition" title="<?= htmlspecialchars($prod['composition']) ?>">
                  <?= htmlspecialchars($prod['composition']) ?>
                </div>
                <ul class="product-specs-list">
                  <li><strong>Category:</strong> <span class="text-truncate"><?= htmlspecialchars($prod['category_name'] ?? 'General') ?></span></li>
                  <li><strong>Strength:</strong> <span><?= htmlspecialchars($prod['strength'] ?? 'Standard') ?></span></li>
                  <li><strong>Packaging:</strong> <span class="text-truncate"><?= htmlspecialchars($prod['packaging'] ?? 'Blister / Bottle') ?></span></li>
                </ul>
              </div>
              <div class="product-card-footer">
                <a href="product-detail.php?slug=<?= urlencode($prod['slug']) ?>" class="btn btn-sm btn-rp-outline flex-grow-1">
                  View Details
                </a>
                <button type="button" class="btn btn-sm btn-rp-secondary" 
                        data-bs-toggle="modal" 
                        data-bs-target="#enquiryModal" 
                        data-product-name="<?= htmlspecialchars($prod['name']) ?>" 
                        data-category-name="<?= htmlspecialchars($prod['category_name'] ?? '') ?>">
                  <i class="fa-solid fa-paper-plane"></i> Enquire
                </button>
              </div>
            </div>
          </div>
          <?php endforeach; ?>
        </div>

      </div>
    </div>
  </div>
</section>

<!-- Call to Action Banner -->
<section class="py-5 text-white" style="background-color: var(--primary);">
  <div class="container py-2 text-center">
    <h3 class="fw-bold text-white mb-2">Can't Find a Specific Dosage Form or Formulation?</h3>
    <p class="text-light lead fs-6 mb-3 mx-auto" style="max-width: 600px;">
      RP PHARMA manufactures custom formulation strengths and packaging configurations through qualified facilities in India.
    </p>
    <a href="contact.php" class="btn btn-rp-secondary">
      <i class="fa-solid fa-file-lines me-2"></i> Submit Custom Requirement
    </a>
  </div>
</section>

<?php
$extra_scripts = '<script src="assets/js/products.js"></script>';
require_once __DIR__ . '/includes/footer.php';
?>
