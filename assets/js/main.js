/**
 * RP PHARMA — Global Frontend Script
 * Includes Opening View / Preloader, Scroll Progress, Sticky Navigation, and Modals
 */

document.addEventListener('DOMContentLoaded', () => {

  /* ------------------------------------------------------------------------
     1. OPENING VIEW / PRELOADER ANIMATION
     ------------------------------------------------------------------------ */
  const preloader = document.getElementById('preloader');
  const preloaderBar = document.getElementById('preloaderBar');
  const preloaderText = document.getElementById('preloaderText');

  if (preloader) {
    let progress = 0;
    const stages = [
      { at: 20, text: 'Initializing Healthcare Network...' },
      { at: 50, text: 'Verifying WHO-GMP Formulations...' },
      { at: 80, text: 'Preparing Global Product Catalogue...' },
      { at: 100, text: 'Welcome to RP PHARMA' }
    ];

    const loadInterval = setInterval(() => {
      progress += Math.floor(Math.random() * 18) + 14;
      if (progress >= 100) {
        progress = 100;
        clearInterval(loadInterval);
        if (preloaderBar) preloaderBar.style.width = '100%';
        if (preloaderText) preloaderText.textContent = 'Welcome to RP PHARMA';

        setTimeout(() => {
          preloader.classList.add('fade-out');
        }, 400);
      } else {
        if (preloaderBar) preloaderBar.style.width = progress + '%';
        for (let i = stages.length - 1; i >= 0; i--) {
          if (progress >= stages[i].at) {
            if (preloaderText) preloaderText.textContent = stages[i].text;
            break;
          }
        }
      }
    }, 80);
  }

  /* ------------------------------------------------------------------------
     2. TOP SCROLL PROGRESS BAR
     ------------------------------------------------------------------------ */
  const scrollProgress = document.getElementById('scrollProgress');
  window.addEventListener('scroll', () => {
    if (scrollProgress) {
      const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
      const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrolled = (height > 0) ? (winScroll / height) * 100 : 0;
      scrollProgress.style.width = scrolled + '%';
    }
  });

  /* ------------------------------------------------------------------------
     3. STICKY NAVBAR & BACK TO TOP BUTTON
     ------------------------------------------------------------------------ */
  const navbar = document.querySelector('.rp-navbar');
  const backToTopBtn = document.getElementById('backToTopBtn');

  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      if (navbar) navbar.classList.add('is-scrolled');
      if (backToTopBtn) backToTopBtn.classList.add('show');
    } else {
      if (navbar) navbar.classList.remove('is-scrolled');
      if (backToTopBtn) backToTopBtn.classList.remove('show');
    }
  });

  if (backToTopBtn) {
    backToTopBtn.addEventListener('click', (e) => {
      e.preventDefault();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  /* ------------------------------------------------------------------------
     4. QUICK ENQUIRY MODAL POPULATOR
     ------------------------------------------------------------------------ */
  const enquiryModal = document.getElementById('enquiryModal');
  if (enquiryModal) {
    enquiryModal.addEventListener('show.bs.modal', function (event) {
      const button = event.relatedTarget;
      if (button) {
        const productName = button.getAttribute('data-product-name');
        const modalProductName = enquiryModal.querySelector('#modalProductName') || enquiryModal.querySelector('#modal_product_name');
        const modalProductInput = enquiryModal.querySelector('#modalProductInput') || enquiryModal.querySelector('#modal_product_name');
        const modalCategoryName = enquiryModal.querySelector('#modalCategoryName') || enquiryModal.querySelector('#modal_category');
        const productCategory = button.getAttribute('data-category-name');

        if (modalProductName && productName) {
          modalProductName.textContent = productName;
          if (modalProductName.tagName === 'INPUT') modalProductName.value = productName;
        }
        if (modalProductInput && productName) {
          modalProductInput.value = productName;
        }
        if (modalCategoryName && productCategory) {
          modalCategoryName.textContent = productCategory;
          if (modalCategoryName.tagName === 'INPUT') modalCategoryName.value = productCategory;
        }
      }
    });
  }
});
