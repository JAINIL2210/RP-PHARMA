<?php
/**
 * RP PHARMA — Footer Component
 */
$site_settings = $site_settings ?? get_site_settings();
?>

  <!-- Corporate Footer -->
  <footer class="rp-footer">
    <div class="container">
      <div class="row g-4">
        
        <!-- Col 1: Brand & Overview -->
        <div class="col-lg-4 col-md-6">
          <div class="d-flex align-items-center gap-2 mb-3">
            <div class="brand-symbol">RP</div>
            <div>
              <span class="fs-5 fw-bold text-white d-block">RP PHARMA</span>
              <span class="text-light" style="font-size:0.75rem;">Healthcare Solutions &bull; Global Exports</span>
            </div>
          </div>
          <p class="small text-muted mb-3 pe-lg-3">
            A global pharmaceutical company headquartered in India, delivering finished formulations and nutraceutical solutions across international healthcare markets.
          </p>
          <div class="d-flex gap-2">
            <span class="badge bg-white bg-opacity-10 text-light border border-white border-opacity-10">WHO-GMP Partner Network</span>
            <span class="badge bg-white bg-opacity-10 text-light border border-white border-opacity-10">Zone IVb Stability</span>
          </div>
        </div>

        <!-- Col 2: Quick Links -->
        <div class="col-lg-2 col-md-6 col-6">
          <h4 class="footer-heading">Company</h4>
          <ul class="footer-links">
            <li><a href="index.php">Home</a></li>
            <li><a href="about.php">About Us</a></li>
            <li><a href="quality.php">Quality &amp; Compliance</a></li>
            <li><a href="manufacturing.php">Manufacturing</a></li>
            <li><a href="global-presence.php">Global Presence</a></li>
            <li><a href="contact.php">Contact Us</a></li>
          </ul>
        </div>

        <!-- Col 3: Product Divisions -->
        <div class="col-lg-3 col-md-6 col-6">
          <h4 class="footer-heading">Formulations</h4>
          <ul class="footer-links">
            <li><a href="pharmaceuticals.php">Pharmaceutical Division</a></li>
            <li><a href="nutraceuticals.php">Nutraceutical Division</a></li>
            <li><a href="products.php?type=pharmaceutical">Finished Antibiotics</a></li>
            <li><a href="products.php?type=pharmaceutical">Cardiovascular Care</a></li>
            <li><a href="products.php?type=nutraceutical">Softgel Supplements</a></li>
            <li><a href="products.php?type=nutraceutical">Vitamins &amp; Minerals</a></li>
          </ul>
        </div>

        <!-- Col 4: Direct Contact -->
        <div class="col-lg-3 col-md-6">
          <h4 class="footer-heading">Direct Contact</h4>
          <ul class="footer-links small text-secondary">
            <li class="mb-2 text-muted">
              <i class="fa-solid fa-location-dot me-2" style="color:var(--accent);"></i> <?= htmlspecialchars($site_settings['office_address'] ?? '[Complete Corporate Office Address], India') ?>
            </li>
            <li class="mb-2">
              <i class="fa-solid fa-phone me-2" style="color:var(--accent);"></i> 
              <a href="tel:<?= htmlspecialchars($site_settings['phone_digits'] ?? '918469034869') ?>" class="text-white fw-bold">
                <?= htmlspecialchars($site_settings['official_phone'] ?? '+91 84690 34869') ?>
              </a>
            </li>
            <li class="mb-2">
              <i class="fa-brands fa-whatsapp me-2 text-success"></i> 
              <a href="https://wa.me/<?= htmlspecialchars($site_settings['whatsapp_raw'] ?? '918469034869') ?>" target="_blank" class="text-white">
                <?= htmlspecialchars($site_settings['whatsapp_number'] ?? '+91 84690 34869') ?>
              </a>
            </li>
            <li class="mb-2">
              <i class="fa-solid fa-envelope me-2" style="color:var(--accent);"></i> 
              <a href="mailto:<?= htmlspecialchars($site_settings['official_email'] ?? 'info@rppharma.com') ?>" class="text-white">
                <?= htmlspecialchars($site_settings['official_email'] ?? 'info@rppharma.com') ?>
              </a>
            </li>
            <li>
              <i class="fa-solid fa-briefcase me-2" style="color:var(--accent);"></i> 
              <a href="mailto:<?= htmlspecialchars($site_settings['business_email'] ?? 'business@rppharma.com') ?>">
                <?= htmlspecialchars($site_settings['business_email'] ?? 'business@rppharma.com') ?>
              </a>
            </li>
          </ul>
        </div>

      </div>

      <!-- Bottom Bar -->
      <div class="footer-bottom d-flex flex-column flex-md-row justify-content-between align-items-center gap-2 text-center text-md-start">
        <div>
          &copy; <?= date('Y') ?> <strong><?= htmlspecialchars($site_settings['company_name'] ?? 'RP PHARMA') ?></strong>. All rights reserved.
        </div>
        <div class="d-flex gap-3">
          <a href="privacy-policy.php" class="text-muted small">Privacy Policy</a>
          <span class="text-muted">&bull;</span>
          <a href="terms.php" class="text-muted small">Terms &amp; Conditions</a>
          <span class="text-muted">&bull;</span>
          <a href="sitemap.xml" class="text-muted small">Sitemap</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- Floating Direct WhatsApp Button -->
  <a href="https://wa.me/<?= htmlspecialchars($site_settings['whatsapp_raw'] ?? '918469034869') ?>?text=Hello%20RP%20PHARMA,%20I%20would%20like%20to%20enquire%20about%20your%20products." 
     class="floating-whatsapp" 
     target="_blank" 
     aria-label="Chat on WhatsApp" 
     title="Chat with RP PHARMA on WhatsApp">
    <i class="fa-brands fa-whatsapp"></i>
  </a>

  <!-- Back to Top Button -->
  <button id="backToTopBtn" class="back-to-top" title="Back to top" aria-label="Back to top">
    <i class="fa-solid fa-arrow-up"></i>
  </button>

  <!-- Universal Product Quick Enquiry Modal -->
  <div class="modal fade" id="enquiryModal" tabindex="-1" aria-labelledby="enquiryModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered modal-lg">
      <div class="modal-content rounded-4 border-0 shadow">
        <div class="modal-header bg-light border-bottom p-4">
          <div>
            <span class="section-tag mb-1"><i class="fa-solid fa-file-signature"></i> Product Enquiry</span>
            <h5 class="modal-title fw-bold text-primary" id="enquiryModalLabel">
              Enquire About: <span id="modalProductName" class="text-dark">Selected Product</span>
            </h5>
            <div class="small text-muted" id="modalCategoryName">Healthcare Formulation</div>
          </div>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>

        <div class="modal-body p-4 p-md-5">
          <form action="api/enquiry.php" method="POST" id="modalEnquiryForm">
            <input type="hidden" name="product_name" id="modalProductInput" value="">
            <input type="hidden" name="enquiry_type" value="product_quotation">
            
            <!-- Honeypot anti-spam -->
            <div style="display:none;" aria-hidden="true">
              <input type="text" name="website_hp" tabindex="-1" autocomplete="off">
            </div>

            <div class="row g-3">
              <div class="col-md-6">
                <label class="form-label-custom">Your Name <span class="text-danger">*</span></label>
                <input type="text" class="form-control form-control-custom" name="full_name" required placeholder="Full Name">
              </div>

              <div class="col-md-6">
                <label class="form-label-custom">Company / Enterprise</label>
                <input type="text" class="form-control form-control-custom" name="company_name" placeholder="Company Name">
              </div>

              <div class="col-md-6">
                <label class="form-label-custom">Email Address <span class="text-danger">*</span></label>
                <input type="email" class="form-control form-control-custom" name="email" required placeholder="name@domain.com">
              </div>

              <div class="col-md-6">
                <label class="form-label-custom">Phone / WhatsApp <span class="text-danger">*</span></label>
                <input type="text" class="form-control form-control-custom" name="phone" required placeholder="+91 / Country Code & Number">
              </div>

              <div class="col-md-6">
                <label class="form-label-custom">Country of Destination <span class="text-danger">*</span></label>
                <input type="text" class="form-control form-control-custom" name="country" required placeholder="Destination Country">
              </div>

              <div class="col-md-6">
                <label class="form-label-custom">Security Check: 3 + 4 = ? <span class="text-danger">*</span></label>
                <input type="hidden" name="captcha_expected" value="7">
                <input type="text" class="form-control form-control-custom" name="captcha_answer" required placeholder="Enter 7">
              </div>

              <div class="col-12">
                <label class="form-label-custom">Requirement Details <span class="text-danger">*</span></label>
                <textarea class="form-control form-control-custom" name="message" rows="3" required placeholder="Specify estimated order volume, packaging preferences, dossier requirements..."></textarea>
              </div>

              <div class="col-12 pt-2">
                <button type="submit" class="btn btn-rp-secondary w-100 py-3 fs-6">
                  <i class="fa-solid fa-paper-plane me-2"></i> Submit Product Enquiry
                </button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>

  <!-- Bootstrap 5 Bundle JS -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
  
  <!-- Main Frontend JS -->
  <script src="assets/js/main.js"></script>

  <?php if (!empty($extra_scripts)) echo $extra_scripts; ?>
</body>
</html>
