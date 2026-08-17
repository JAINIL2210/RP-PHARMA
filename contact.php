<?php
/**
 * RP PHARMA — Contact Us Page
 */
$page_title = 'Contact RP PHARMA | Direct Phone: +91 84690 34869';
$page_desc = 'Contact RP PHARMA corporate & export headquarters. Call or WhatsApp +91 84690 34869 for pharmaceutical and nutraceutical supply inquiries.';

require_once __DIR__ . '/includes/header.php';

$status = $_GET['status'] ?? null;
?>

<!-- Header Banner -->
<section class="py-5" style="background: linear-gradient(180deg, #F0F6FA 0%, #FFFFFF 100%); border-bottom:1px solid var(--border-color);">
  <div class="container py-3">
    <div class="row align-items-center">
      <div class="col-lg-8">
        <nav aria-label="breadcrumb">
          <ol class="breadcrumb small mb-2">
            <li class="breadcrumb-item"><a href="index.php">Home</a></li>
            <li class="breadcrumb-item active" aria-current="page">Contact Us</li>
          </ol>
        </nav>
        <span class="section-tag"><i class="fa-solid fa-headset"></i> Immediate Support &amp; Enquiries</span>
        <h1 class="display-6 fw-bold text-primary mb-2">Contact RP PHARMA</h1>
        <p class="lead text-body fs-6 mb-0">
          Reach out to our export desk and commercial teams for product catalogs, pricing quotations, and global partnership inquiries.
        </p>
      </div>
    </div>
  </div>
</section>

<!-- Direct Contact Highlights Bar -->
<section class="py-4 bg-white border-bottom">
  <div class="container">
    <div class="row g-3 justify-content-center">
      
      <!-- Phone Call Card -->
      <div class="col-md-4">
        <div class="p-3 p-xl-4 rounded-4 bg-light border h-100 d-flex align-items-center gap-3">
          <div class="rounded-3 p-3 d-flex align-items-center justify-content-center" style="width:52px;height:52px;font-size:1.35rem;background-color:var(--primary);color:#FFFFFF;">
            <i class="fa-solid fa-phone"></i>
          </div>
          <div class="flex-grow-1">
            <div class="small text-muted fw-semibold">Direct Call Support</div>
            <a href="tel:<?= htmlspecialchars($site_settings['phone_digits'] ?? '918469034869') ?>" class="fs-5 fw-bold text-primary text-decoration-none d-block">
              <?= htmlspecialchars($site_settings['official_phone'] ?? '+91 84690 34869') ?>
            </a>
            <span class="badge bg-success bg-opacity-10 text-success small py-1 px-2 mt-1">Mon - Sat Available</span>
          </div>
        </div>
      </div>

      <!-- WhatsApp Card -->
      <div class="col-md-4">
        <div class="p-3 p-xl-4 rounded-4 bg-light border h-100 d-flex align-items-center gap-3">
          <div class="rounded-3 p-3 d-flex align-items-center justify-content-center text-white" style="width:52px;height:52px;font-size:1.6rem;background-color:#25D366;">
            <i class="fa-brands fa-whatsapp"></i>
          </div>
          <div class="flex-grow-1">
            <div class="small text-muted fw-semibold">Instant WhatsApp Chat</div>
            <a href="https://wa.me/<?= htmlspecialchars($site_settings['whatsapp_raw'] ?? '918469034869') ?>?text=Hello%20RP%20PHARMA,%20I%20would%20like%20to%20enquire%20about%20your%20products." target="_blank" class="fs-5 fw-bold text-success text-decoration-none d-block">
              <?= htmlspecialchars($site_settings['whatsapp_number'] ?? '+91 84690 34869') ?>
            </a>
            <span class="small text-muted">Click to chat directly</span>
          </div>
        </div>
      </div>

      <!-- Email Card -->
      <div class="col-md-4">
        <div class="p-3 p-xl-4 rounded-4 bg-light border h-100 d-flex align-items-center gap-3">
          <div class="rounded-3 p-3 d-flex align-items-center justify-content-center" style="width:52px;height:52px;font-size:1.35rem;background-color:var(--primary);color:#FFFFFF;">
            <i class="fa-solid fa-envelope"></i>
          </div>
          <div class="flex-grow-1">
            <div class="small text-muted fw-semibold">Official Email Desk</div>
            <a href="mailto:<?= htmlspecialchars($site_settings['official_email'] ?? 'info@rppharma.com') ?>" class="fw-bold text-primary text-decoration-none text-truncate d-block">
              <?= htmlspecialchars($site_settings['official_email'] ?? 'info@rppharma.com') ?>
            </a>
            <span class="small text-muted">Business: <?= htmlspecialchars($site_settings['business_email'] ?? 'business@rppharma.com') ?></span>
          </div>
        </div>
      </div>

    </div>
  </div>
</section>

<!-- Contact Form & Details Section -->
<section class="py-5 bg-light">
  <div class="container">

    <!-- Flash Status Messages -->
    <?php if ($status === 'success'): ?>
    <div class="alert alert-success alert-dismissible fade show rounded-3 p-3 mb-4" role="alert">
      <i class="fa-solid fa-circle-check me-2"></i> <strong>Thank you!</strong> Your message has been successfully submitted. Our commercial export team will get in touch with you shortly.
      <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>
    <?php elseif ($status === 'captcha_error'): ?>
    <div class="alert alert-danger alert-dismissible fade show rounded-3 p-3 mb-4" role="alert">
      <i class="fa-solid fa-triangle-exclamation me-2"></i> <strong>Verification Failed:</strong> Please enter the correct answer to the security question.
      <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>
    <?php elseif ($status === 'required_missing'): ?>
    <div class="alert alert-warning alert-dismissible fade show rounded-3 p-3 mb-4" role="alert">
      <i class="fa-solid fa-circle-exclamation me-2"></i> <strong>Missing Information:</strong> Please fill in all required fields.
      <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>
    <?php endif; ?>

    <div class="row g-4 align-items-stretch">
      
      <!-- Left Column: Contact Form -->
      <div class="col-lg-7">
        <div class="p-4 p-md-5 rounded-4 border bg-white shadow-sm h-100">
          <div class="d-flex align-items-center gap-2 mb-4 pb-2 border-bottom">
            <i class="fa-solid fa-paper-plane text-primary fs-4"></i>
            <h3 class="fw-bold fs-4 text-primary mb-0">Send an Enquiry</h3>
          </div>

          <form action="api/enquiry.php" method="POST">
            <input type="hidden" name="enquiry_type" value="general_contact">
            
            <!-- Honeypot Anti-Spam Field -->
            <div style="display:none;" aria-hidden="true">
              <input type="text" name="website_hp" tabindex="-1" autocomplete="off">
            </div>

            <div class="row g-3">
              <div class="col-md-6">
                <label class="form-label form-label-custom">Your Name <span class="text-danger">*</span></label>
                <input type="text" class="form-control form-control-custom" name="full_name" required placeholder="Full Name">
              </div>

              <div class="col-md-6">
                <label class="form-label form-label-custom">Company / Enterprise</label>
                <input type="text" class="form-control form-control-custom" name="company_name" placeholder="Company Name">
              </div>

              <div class="col-md-6">
                <label class="form-label form-label-custom">Email Address <span class="text-danger">*</span></label>
                <input type="email" class="form-control form-control-custom" name="email" required placeholder="name@domain.com">
              </div>

              <div class="col-md-6">
                <label class="form-label form-label-custom">Phone / WhatsApp <span class="text-danger">*</span></label>
                <input type="text" class="form-control form-control-custom" name="phone" required placeholder="+91 / Country Code & Number">
              </div>

              <div class="col-md-6">
                <label class="form-label form-label-custom">Country of Operation <span class="text-danger">*</span></label>
                <input type="text" class="form-control form-control-custom" name="country" required placeholder="e.g. India, UAE, Vietnam, Kenya">
              </div>

              <div class="col-md-6">
                <label class="form-label form-label-custom">Subject <span class="text-danger">*</span></label>
                <input type="text" class="form-control form-control-custom" name="subject" required placeholder="Product Enquiry / Distribution / Dossier">
              </div>

              <div class="col-12">
                <label class="form-label form-label-custom">Enquiry Message <span class="text-danger">*</span></label>
                <textarea class="form-control form-control-custom" name="message" rows="4" required placeholder="Please describe your requirements, formulation interest, or estimated order volume..."></textarea>
              </div>

              <!-- Security Check -->
              <div class="col-md-6">
                <label class="form-label form-label-custom">Security Question: 4 + 4 = ? <span class="text-danger">*</span></label>
                <input type="hidden" name="captcha_expected" value="8">
                <input type="text" class="form-control form-control-custom" name="captcha_answer" required placeholder="Enter 8">
              </div>

              <div class="col-12 pt-2">
                <button type="submit" class="btn btn-rp-secondary w-100 py-3 fs-6">
                  <i class="fa-solid fa-paper-plane me-2"></i> Submit Message
                </button>
              </div>
            </div>
          </form>
        </div>
      </div>

      <!-- Right Column: Corporate Details & Working Hours -->
      <div class="col-lg-5">
        <div class="p-4 p-md-5 rounded-4 border bg-white shadow-sm h-100 d-flex flex-column justify-content-between">
          <div>
            <div class="d-flex align-items-center gap-2 mb-4 pb-2 border-bottom">
              <i class="fa-solid fa-building text-primary fs-4"></i>
              <h3 class="fw-bold fs-4 text-primary mb-0">Corporate Office</h3>
            </div>

            <!-- Address Card -->
            <div class="mb-4">
              <div class="d-flex gap-3 align-items-start">
                <i class="fa-solid fa-location-dot fs-5 mt-1" style="color:var(--accent);"></i>
                <div>
                  <h6 class="fw-bold text-primary mb-1">Registered &amp; Corporate Office</h6>
                  <p class="text-muted small mb-0"><?= htmlspecialchars($site_settings['office_address'] ?? '[Complete Corporate Office Address], India') ?></p>
                </div>
              </div>
            </div>

            <!-- Working Hours -->
            <div class="mb-4">
              <div class="d-flex gap-3 align-items-start">
                <i class="fa-regular fa-clock fs-5 mt-1" style="color:var(--accent);"></i>
                <div>
                  <h6 class="fw-bold text-primary mb-1">Business Hours</h6>
                  <p class="text-muted small mb-0"><?= htmlspecialchars($site_settings['working_hours'] ?? 'Monday – Saturday: 9:00 AM – 6:30 PM (IST)') ?></p>
                  <p class="text-muted small mb-0">Sunday: Closed (Emergency export desk on WhatsApp)</p>
                </div>
              </div>
            </div>

            <!-- Departments Direct -->
            <div class="mb-4 pt-3 border-top">
              <h6 class="fw-bold text-primary mb-3">Key Contact Departments</h6>
              <div class="d-flex flex-column gap-2 small">
                <div class="d-flex justify-content-between">
                  <span class="text-muted">General Enquiries:</span>
                  <a href="mailto:<?= htmlspecialchars($site_settings['official_email'] ?? 'info@rppharma.com') ?>" class="fw-semibold"><?= htmlspecialchars($site_settings['official_email'] ?? 'info@rppharma.com') ?></a>
                </div>
                <div class="d-flex justify-content-between">
                  <span class="text-muted">Business Partnerships:</span>
                  <a href="mailto:<?= htmlspecialchars($site_settings['business_email'] ?? 'business@rppharma.com') ?>" class="fw-semibold"><?= htmlspecialchars($site_settings['business_email'] ?? 'business@rppharma.com') ?></a>
                </div>
                <div class="d-flex justify-content-between">
                  <span class="text-muted">Export Documentation:</span>
                  <a href="mailto:<?= htmlspecialchars($site_settings['export_email'] ?? 'export@rppharma.com') ?>" class="fw-semibold"><?= htmlspecialchars($site_settings['export_email'] ?? 'export@rppharma.com') ?></a>
                </div>
              </div>
            </div>
          </div>

          <!-- Quick Action Buttons -->
          <div class="pt-3 border-top">
            <div class="row g-2">
              <div class="col-6">
                <a href="tel:<?= htmlspecialchars($site_settings['phone_digits'] ?? '918469034869') ?>" class="btn btn-rp-outline w-100 btn-sm py-2">
                  <i class="fa-solid fa-phone me-1"></i> Call Now
                </a>
              </div>
              <div class="col-6">
                <a href="https://wa.me/<?= htmlspecialchars($site_settings['whatsapp_raw'] ?? '918469034869') ?>" target="_blank" class="btn btn-rp-secondary w-100 btn-sm py-2">
                  <i class="fa-brands fa-whatsapp me-1"></i> WhatsApp
                </a>
              </div>
            </div>
          </div>

        </div>
      </div>

    </div>
  </div>
</section>

<?php require_once __DIR__ . '/includes/footer.php'; ?>
