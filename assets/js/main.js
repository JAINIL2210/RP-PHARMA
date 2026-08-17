/**
 * RP PHARMA — Global Frontend Script
 */

document.addEventListener('DOMContentLoaded', () => {
  // Sticky Navbar shadow on scroll
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

  // Back to top click
  if (backToTopBtn) {
    backToTopBtn.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // Populate Enquiry Modal when triggered from a product card
  const enquiryModal = document.getElementById('enquiryModal');
  if (enquiryModal) {
    enquiryModal.addEventListener('show.bs.modal', function (event) {
      const button = event.relatedTarget;
      if (button) {
        const productName = button.getAttribute('data-product-name');
        const modalProductName = enquiryModal.querySelector('#modalProductName');
        const modalProductInput = enquiryModal.querySelector('#modalProductInput');
        const modalCategoryName = enquiryModal.querySelector('#modalCategoryName');
        const productCategory = button.getAttribute('data-category-name');

        if (modalProductName && productName) {
          modalProductName.textContent = productName;
        }
        if (modalProductInput && productName) {
          modalProductInput.value = productName;
        }
        if (modalCategoryName && productCategory) {
          modalCategoryName.textContent = productCategory;
        }
      }
    });
  }
});
