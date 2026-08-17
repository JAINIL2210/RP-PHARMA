/**
 * RP PHARMA — Global Frontend Script
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Sticky Navbar styling on scroll
  const navbar = document.querySelector('.rp-navbar');
  const backToTop = document.querySelector('.back-to-top');

  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      if (navbar) navbar.classList.add('is-scrolled');
      if (backToTop) backToTop.classList.add('show');
    } else {
      if (navbar) navbar.classList.remove('is-scrolled');
      if (backToTop) backToTop.classList.remove('show');
    }
  });

  // 2. Back to top action
  if (backToTop) {
    backToTop.addEventListener('click', (e) => {
      e.preventDefault();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // 3. Trust Counter Animation (Count-up on scroll view)
  const counterElements = document.querySelectorAll('.stat-counter');
  if (counterElements.length > 0) {
    const animateCounter = (el) => {
      const targetStr = el.getAttribute('data-target') || '0';
      const cleanNum = parseInt(targetStr.replace(/[^0-9]/g, '')) || 0;
      const suffix = targetStr.replace(/[0-9]/g, '');
      
      let start = 0;
      const duration = 1600;
      const stepTime = 25;
      const steps = duration / stepTime;
      const increment = cleanNum / steps;

      const timer = setInterval(() => {
        start += increment;
        if (start >= cleanNum) {
          el.innerText = `${cleanNum}${suffix}`;
          clearInterval(timer);
        } else {
          el.innerText = `${Math.floor(start)}${suffix}`;
        }
      }, stepTime);
    };

    const counterObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.2 });

    counterElements.forEach(el => counterObserver.observe(el));
  }

  // 4. Pre-fill Enquiry Modal when clicking "Enquire Now" on any card
  const enquiryModal = document.getElementById('enquiryModal');
  if (enquiryModal) {
    enquiryModal.addEventListener('show.bs.modal', function (event) {
      const button = event.relatedTarget;
      if (button) {
        const productName = button.getAttribute('data-product-name');
        const categoryName = button.getAttribute('data-category-name');
        
        const modalProdInput = enquiryModal.querySelector('#modal_product_name');
        const modalCatInput = enquiryModal.querySelector('#modal_category');
        const modalTitle = enquiryModal.querySelector('#enquiryModalLabel');
        
        if (modalProdInput && productName) {
          modalProdInput.value = productName;
        }
        if (modalCatInput && categoryName) {
          modalCatInput.value = categoryName;
        }
        if (modalTitle && productName) {
          modalTitle.textContent = `Enquire About: ${productName}`;
        }
      }
    });
  }

  // 5. Auto dismiss flash alerts after 6 seconds
  const flashAlerts = document.querySelectorAll('.alert-dismissible');
  flashAlerts.forEach(alert => {
    setTimeout(() => {
      try {
        const bsAlert = new bootstrap.Alert(alert);
        bsAlert.close();
      } catch (e) {}
    }, 6000);
  });
});
