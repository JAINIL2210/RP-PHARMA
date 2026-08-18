<?php
/**
 * RP PHARMA — Header Component
 */
require_once __DIR__ . '/functions.php';

$site_settings = get_site_settings();
$pharma_nav_cats = get_categories('pharmaceutical');
$nutra_nav_cats = get_categories('nutraceutical');

$current_page = basename($_SERVER['PHP_SELF'], '.php');
$page_title = $page_title ?? 'RP PHARMA | Pharmaceutical & Nutraceutical Solutions India';
$page_desc = $page_desc ?? 'RP PHARMA is a global pharmaceutical company headquartered in India delivering high-quality finished formulations and nutraceutical solutions.';
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title><?= htmlspecialchars($page_title) ?></title>
  <meta name="description" content="<?= htmlspecialchars($page_desc) ?>">
  <meta name="robots" content="index, follow">
  
  <!-- Open Graph -->
  <meta property="og:title" content="<?= htmlspecialchars($page_title) ?>">
  <meta property="og:description" content="<?= htmlspecialchars($page_desc) ?>">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="RP PHARMA">
  
  <!-- Bootstrap 5 CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  
  <!-- FontAwesome 6 Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  
  <!-- Custom Modern Medical Theme CSS -->
  <link rel="stylesheet" href="assets/css/style.css">
  
  <?php if (!empty($extra_head)) echo $extra_head; ?>
</head>
<body>

  <!-- Top Scroll Progress Indicator -->
  <div class="scroll-progress" id="scrollProgress"></div>

  <!-- Interactive Particle Background Canvas -->
  <canvas id="particle-canvas"></canvas>
  <div class="mouse-spotlight" id="mouseSpotlight"></div>

  <!-- Custom Glowing Cursor (Desktop) -->
  <div class="custom-cursor-dot" id="cursorDot"></div>
  <div class="custom-cursor-ring" id="cursorRing"></div>

  <!-- Preloader Opening Screen -->
  <div id="preloader">
    <div class="preloader-content">
      <div class="preloader-logo">&lt;RP PHARMA /&gt;</div>
      <div class="preloader-bar-bg">
        <div class="preloader-bar" id="preloaderBar"></div>
      </div>
      <div class="preloader-text" id="preloaderText">Initializing Healthcare Network...</div>
    </div>
  </div>

  <!-- Top Utility Contact Bar -->
  <div class="top-bar">
    <div class="container d-flex flex-wrap justify-content-between align-items-center gap-2">
      <div class="d-flex align-items-center gap-3">
        <span class="info-pill d-none d-sm-inline">
          <i class="fa-solid fa-earth-americas" style="color:var(--accent);"></i> Global Healthcare Exporter
        </span>
        <span class="info-pill d-none d-md-inline">
          <i class="fa-solid fa-clock" style="color:var(--accent);"></i> <?= htmlspecialchars($site_settings['working_hours'] ?? 'Mon - Sat: 9:00 AM - 6:30 PM') ?>
        </span>
      </div>

      <div class="d-flex align-items-center gap-3 ms-auto">
        <!-- Direct Phone Call -->
        <a href="tel:<?= htmlspecialchars($site_settings['phone_digits'] ?? '918469034869') ?>" class="info-pill fw-semibold">
          <i class="fa-solid fa-phone" style="color:var(--accent);"></i> <?= htmlspecialchars($site_settings['official_phone'] ?? '+91 84690 34869') ?>
        </a>

        <!-- Direct WhatsApp -->
        <a href="https://wa.me/<?= htmlspecialchars($site_settings['whatsapp_raw'] ?? '918469034869') ?>" target="_blank" class="info-pill fw-semibold text-white">
          <i class="fa-brands fa-whatsapp text-success"></i> WhatsApp
        </a>

        <!-- Email -->
        <a href="mailto:<?= htmlspecialchars($site_settings['official_email'] ?? 'info@rppharma.com') ?>" class="info-pill d-none d-lg-inline">
          <i class="fa-regular fa-envelope" style="color:var(--accent);"></i> <?= htmlspecialchars($site_settings['official_email'] ?? 'info@rppharma.com') ?>
        </a>
      </div>
    </div>
  </div>

  <!-- Main Navigation Bar -->
  <nav class="navbar navbar-expand-lg rp-navbar">
    <div class="container">
      
      <!-- Brand Logo -->
      <a class="navbar-brand navbar-brand-logo" href="index.php">
        <div class="brand-symbol">RP</div>
        <div class="brand-text-wrap">
          <span class="brand-title">RP PHARMA</span>
          <span class="brand-subtitle">Healthcare &bull; Global</span>
        </div>
      </a>

      <!-- Quick Call Button for Mobile -->
      <a href="tel:<?= htmlspecialchars($site_settings['phone_digits'] ?? '918469034869') ?>" class="btn btn-sm btn-rp-outline d-lg-none ms-auto me-2 px-2 py-1" style="min-height:36px;" title="Call RP PHARMA">
        <i class="fa-solid fa-phone"></i>
      </a>

      <!-- Mobile Hamburger Toggle -->
      <button class="navbar-toggler border-0 shadow-none p-1" type="button" data-bs-toggle="collapse" data-bs-target="#mainNavbarNav" aria-controls="mainNavbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <!-- Nav Links -->
      <div class="collapse navbar-collapse" id="mainNavbarNav">
        <ul class="navbar-nav ms-auto align-items-lg-center gap-lg-1 my-2 my-lg-0">
          <li class="nav-item">
            <a class="nav-link nav-link-custom <?= $current_page === 'index' ? 'active' : '' ?>" href="index.php">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link nav-link-custom <?= $current_page === 'about' ? 'active' : '' ?>" href="about.php">About Us</a>
          </li>
          <li class="nav-item">
            <a class="nav-link nav-link-custom <?= $current_page === 'pharmaceuticals' ? 'active' : '' ?>" href="pharmaceuticals.php">Pharmaceuticals</a>
          </li>
          <li class="nav-item">
            <a class="nav-link nav-link-custom <?= $current_page === 'nutraceuticals' ? 'active' : '' ?>" href="nutraceuticals.php">Nutraceuticals</a>
          </li>
          <li class="nav-item">
            <a class="nav-link nav-link-custom <?= $current_page === 'products' || $current_page === 'product-detail' ? 'active' : '' ?>" href="products.php">Catalogue</a>
          </li>
          <li class="nav-item">
            <a class="nav-link nav-link-custom <?= $current_page === 'quality' ? 'active' : '' ?>" href="quality.php">Quality</a>
          </li>
          <li class="nav-item">
            <a class="nav-link nav-link-custom <?= $current_page === 'manufacturing' ? 'active' : '' ?>" href="manufacturing.php">Manufacturing</a>
          </li>
          <li class="nav-item">
            <a class="nav-link nav-link-custom <?= $current_page === 'global-presence' ? 'active' : '' ?>" href="global-presence.php">Global Presence</a>
          </li>
          <li class="nav-item">
            <a class="nav-link nav-link-custom <?= $current_page === 'contact' ? 'active' : '' ?>" href="contact.php">Contact Us</a>
          </li>
          <li class="nav-item ms-lg-2 mt-2 mt-lg-0">
            <a href="contact.php" class="btn btn-rp-secondary btn-sm-custom w-100">
              <i class="fa-solid fa-paper-plane"></i> Business Enquiry
            </a>
          </li>
        </ul>
      </div>

    </div>
  </nav>
