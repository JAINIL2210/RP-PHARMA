<?php
/**
 * RP PHARMA — Product Detail Page
 */
require_once __DIR__ . '/includes/functions.php';

$slug = isset($_GET['slug']) ? trim($_GET['slug']) : '';
$product = $slug ? get_product_by_slug($slug) : null;

if (!$product) {
    header('Location: products.php');
    exit;
}

$page_title = htmlspecialchars($product['name']) . ' | RP PHARMA Pharmaceutical & Nutraceutical Solutions';
$page_desc = htmlspecialchars($product['name']) . ' (' . htmlspecialchars($product['composition']) . '). Dosage form: ' . htmlspecialchars($product['dosage_form']) . ', strength: ' . htmlspecialchars($product['strength'] ?? '') . '. Supplied with CTD dossiers and stability data.';

// Schema.org JSON-LD structured data
$extra_head = '
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": ' . json_encode($product['name']) . ',
  "description": ' . json_encode($product['description'] ?? $product['composition']) . ',
  "category": ' . json_encode($product['category_name'] ?? $product['type']) . ',
  "brand": {
    "@type": "Brand",
    "name": "RP PHARMA"
  },
  "offers": {
    "@type": "Offer",
    "availability": "https://schema.org/InStock",
    "priceCurrency": "USD",
    "price": "Contact for B2B Pricing"
  }
}
</script>
';

require_once __DIR__ . '/includes/header.php';

// Get Related Products in same category
$related_products = [];
if (!empty($product['category_slug'])) {
    $related = get_products(['category_slug' => $product['category_slug']]);
    $related_products = array_values(array_filter($related, fn($p) => $p['slug'] !== $product['slug']));
    $related_products = array_slice($related_products, 0, 3);
}
?>

<!-- Header Banner -->
<section class="py-4" style="background: linear-gradient(180deg, #F0F6FA 0%, #FFFFFF 100%); border-bottom:1px solid var(--border-color);">
  <div class="container">
    <nav aria-label="breadcrumb">
      <ol class="breadcrumb small mb-2">
        <li class="breadcrumb-item"><a href="index.php">Home</a></li>
        <li class="breadcrumb-item"><a href="products.php">Products</a></li>
        <?php if (!empty($product['category_name'])): ?>
        <li class="breadcrumb-item"><a href="products.php?category=<?= urlencode($product['category_slug'] ?? '') ?>"><?= htmlspecialchars($product['category_name']) ?></a></li>
        <?php endif; ?>
        <li class="breadcrumb-item active text-truncate" aria-current="page" style="max-width: 250px;"><?= htmlspecialchars($product['name']) ?></li>
      </ol>
    </nav>
  </div>
</section>

<!-- Product Details Main Section -->
<section class="py-5 bg-white">
  <div class="container py-2">
    <div class="row g-4 g-lg-5">
      
      <!-- Left Column: Product Overview & Badges -->
      <div class="col-lg-5">
        <div class="p-4 rounded-4 border bg-light text-center mb-4">
          <div class="d-inline-flex align-items-center justify-content-center p-3 bg-white rounded-circle shadow-sm mb-3" style="width:100px;height:100px;">
            <i class="fa-solid <?= $product['type'] === 'pharmaceutical' ? 'fa-tablets text-primary' : 'fa-leaf text-accent' ?> fs-1" style="color:var(--primary);"></i>
          </div>
          <div class="mb-2">
            <span class="product-type-badge <?= $product['type'] === 'pharmaceutical' ? 'badge-pharma' : 'badge-nutra' ?> px-3 py-1 fs-6">
              <?= ucfirst($product['type']) ?> Formulation
            </span>
          </div>
          <h2 class="fw-bold text-primary fs-4 mt-2 mb-1"><?= htmlspecialchars($product['name']) ?></h2>
          <p class="text-muted small mb-0"><?= htmlspecialchars($product['category_name'] ?? 'Healthcare Segment') ?></p>
        </div>

        <!-- Technical Verification Badges -->
        <div class="p-4 rounded-4 bg-light border">
          <h5 class="fw-bold fs-6 text-primary mb-3"><i class="fa-solid fa-file-circle-check me-2" style="color:var(--accent);"></i> Quality &amp; Compliance</h5>
          <ul class="list-unstyled small mb-0">
            <li class="mb-2 d-flex align-items-start gap-2">
              <i class="fa-solid fa-check text-primary mt-1"></i>
              <span><strong>Manufacturing:</strong> Qualified facilities in India complying with WHO-GMP.</span>
            </li>
            <li class="mb-2 d-flex align-items-start gap-2">
              <i class="fa-solid fa-check text-primary mt-1"></i>
              <span><strong>Pharmacopeia:</strong> Formulated in compliance with IP / BP / USP monographs.</span>
            </li>
            <li class="mb-2 d-flex align-items-start gap-2">
              <i class="fa-solid fa-check text-primary mt-1"></i>
              <span><strong>Batch Testing:</strong> Comprehensive Certificate of Analysis (COA) issued per lot.</span>
            </li>
            <li class="d-flex align-items-start gap-2">
              <i class="fa-solid fa-check text-primary mt-1"></i>
              <span><strong>Climatic Zone:</strong> Stability testing under ICH Zone IVb conditions where applicable.</span>
            </li>
          </ul>
        </div>
      </div>

      <!-- Right Column: Detailed Product Profile & Specifications -->
      <div class="col-lg-7">
        <h1 class="display-6 fw-bold text-primary mb-2"><?= htmlspecialchars($product['name']) ?></h1>
        <p class="lead text-muted fs-6 mb-4"><?= htmlspecialchars($product['indications'] ?? 'Therapeutic Formulation for International B2B Markets') ?></p>

        <!-- Action CTAs -->
        <div class="d-flex flex-column flex-sm-row flex-wrap gap-2 gap-sm-3 mb-4 pb-4 border-bottom">
          <button type="button" class="btn btn-rp-secondary" data-bs-toggle="modal" data-bs-target="#enquiryModal" data-product-name="<?= htmlspecialchars($product['name']) ?>" data-category-name="<?= htmlspecialchars($product['category_name'] ?? '') ?>">
            <i class="fa-solid fa-paper-plane me-1"></i> Send Enquiry / Get Quotation
          </button>
          <a href="tel:<?= htmlspecialchars($site_settings['phone_digits'] ?? '918469034869') ?>" class="btn btn-rp-outline">
            <i class="fa-solid fa-phone me-1"></i> Call <?= htmlspecialchars($site_settings['official_phone'] ?? '+91 84690 34869') ?>
          </a>
        </div>

        <!-- Specifications Table -->
        <h4 class="fw-bold fs-5 text-primary mb-3">Product Specifications</h4>
        <div class="table-responsive mb-4">
          <table class="table table-bordered align-middle">
            <tbody>
              <tr>
                <th class="bg-light text-dark" style="width: 35%;">Composition</th>
                <td class="text-body fw-semibold"><?= htmlspecialchars($product['composition']) ?></td>
              </tr>
              <tr>
                <th class="bg-light text-dark">Dosage Form</th>
                <td><?= htmlspecialchars($product['dosage_form']) ?></td>
              </tr>
              <tr>
                <th class="bg-light text-dark">Strength / Potency</th>
                <td><?= htmlspecialchars($product['strength'] ?? 'Standard Export Strength') ?></td>
              </tr>
              <tr>
                <th class="bg-light text-dark">Packaging Style</th>
                <td><?= htmlspecialchars($product['packaging'] ?? 'Alu-Alu Blister / Strip / HDPE Container') ?></td>
              </tr>
              <tr>
                <th class="bg-light text-dark">Therapeutic Segment</th>
                <td><?= htmlspecialchars($product['category_name'] ?? 'Healthcare Formulation') ?></td>
              </tr>
              <tr>
                <th class="bg-light text-dark">Available Markets</th>
                <td><?= htmlspecialchars($product['available_markets'] ?? 'Asia, Africa, Middle East, CIS, Latin America') ?></td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- Technical & Regulatory Status -->
        <h4 class="fw-bold fs-5 text-primary mb-3">Technical Documentation Availability</h4>
        <div class="row g-3 mb-4">
          <div class="col-sm-6">
            <div class="p-3 bg-light rounded-3 border">
              <div class="fw-bold text-primary small mb-1"><i class="fa-solid fa-file-shield me-2" style="color:var(--accent);"></i> Regulatory Dossier</div>
              <div class="small text-muted"><?= htmlspecialchars($product['dossier_status'] ?? 'CTD / ACTD Dossier Available on Request') ?></div>
            </div>
          </div>
          <div class="col-sm-6">
            <div class="p-3 bg-light rounded-3 border">
              <div class="fw-bold text-primary small mb-1"><i class="fa-solid fa-vial-circle-check me-2" style="color:var(--accent);"></i> Stability Studies</div>
              <div class="small text-muted"><?= htmlspecialchars($product['stability_status'] ?? 'Zone IVb Stability Tested') ?></div>
            </div>
          </div>
          <div class="col-sm-6">
            <div class="p-3 bg-light rounded-3 border">
              <div class="fw-bold text-primary small mb-1"><i class="fa-solid fa-clipboard-check me-2" style="color:var(--accent);"></i> Process Validation</div>
              <div class="small text-muted"><?= htmlspecialchars($product['validation_status'] ?? 'Validated Manufacturing Process') ?></div>
            </div>
          </div>
          <div class="col-sm-6">
            <div class="p-3 bg-light rounded-3 border">
              <div class="fw-bold text-primary small mb-1"><i class="fa-solid fa-stamp me-2" style="color:var(--accent);"></i> Quality Certificate</div>
              <div class="small text-muted"><?= htmlspecialchars($product['coa_status'] ?? 'Certificate of Analysis per Batch') ?></div>
            </div>
          </div>
        </div>

        <!-- Description -->
        <?php if (!empty($product['description'])): ?>
        <h4 class="fw-bold fs-5 text-primary mb-2">Product Description</h4>
        <p class="text-body mb-4"><?= htmlspecialchars($product['description']) ?></p>
        <?php endif; ?>

      </div>
    </div>
  </div>
</section>

<!-- Related Products Section -->
<?php if (!empty($related_products)): ?>
<section class="py-5 bg-light">
  <div class="container py-2">
    <div class="d-flex flex-column flex-sm-row justify-content-between align-items-sm-center mb-4">
      <h3 class="fw-bold text-primary fs-5 mb-2 mb-sm-0">Related Formulations in <?= htmlspecialchars($product['category_name'] ?? 'this Segment') ?></h3>
      <a href="products.php?category=<?= urlencode($product['category_slug'] ?? '') ?>" class="btn btn-sm btn-rp-outline">
        View All in Category <i class="fa-solid fa-arrow-right ms-1"></i>
      </a>
    </div>

    <div class="row g-3 g-md-4">
      <?php foreach ($related_products as $rel): ?>
      <div class="col-sm-6 col-md-4">
        <div class="product-card">
          <div class="product-card-header">
            <span class="product-type-badge <?= $rel['type'] === 'pharmaceutical' ? 'badge-pharma' : 'badge-nutra' ?>">
              <?= ucfirst($rel['type']) ?>
            </span>
            <span class="small text-muted"><?= htmlspecialchars($rel['dosage_form']) ?></span>
          </div>
          <div class="product-card-body">
            <h5 class="product-title"><?= htmlspecialchars($rel['name']) ?></h5>
            <div class="product-composition"><?= htmlspecialchars($rel['composition']) ?></div>
          </div>
          <div class="product-card-footer">
            <a href="product-detail.php?slug=<?= urlencode($rel['slug']) ?>" class="btn btn-sm btn-rp-outline flex-grow-1">View Details</a>
            <button type="button" class="btn btn-sm btn-rp-secondary" data-bs-toggle="modal" data-bs-target="#enquiryModal" data-product-name="<?= htmlspecialchars($rel['name']) ?>" data-category-name="<?= htmlspecialchars($rel['category_name'] ?? '') ?>">
              Enquire
            </button>
          </div>
        </div>
      </div>
      <?php endforeach; ?>
    </div>
  </div>
</section>
<?php endif; ?>

<?php require_once __DIR__ . '/includes/footer.php'; ?>
