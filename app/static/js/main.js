/**
 * RP PHARMA — Interactive Frontend & Animation Engine
 * Features:
 * 1. Preloader Screen & Opening Sequence
 * 2. Interactive Particle Network Background Canvas
 * 3. Mouse Spotlight & Custom Smooth Cursor
 * 4. Top Scroll Progress Line
 * 5. Scroll Reveal Intersection Observers
 * 6. Hero 3D Card Perspective Tilt
 * 7. Sticky Navbar & Modal Autofill
 */

document.addEventListener('DOMContentLoaded', () => {

  /* ------------------------------------------------------------------------
     1. PRELOADER & OPENING VIEW SEQUENCE
     ------------------------------------------------------------------------ */
  const preloader = document.getElementById('preloader');
  const preloaderBar = document.getElementById('preloaderBar');
  const preloaderText = document.getElementById('preloaderText');

  let progress = 0;
  const stages = [
    { at: 20, text: 'Initializing Healthcare Environment...' },
    { at: 50, text: 'Verifying WHO-GMP Formulations...' },
    { at: 80, text: 'Loading Global Product Catalogue...' },
    { at: 100, text: 'System Ready!' }
  ];

  const loadInterval = setInterval(() => {
    progress += Math.floor(Math.random() * 16) + 12;
    if (progress >= 100) {
      progress = 100;
      clearInterval(loadInterval);
      if (preloaderBar) preloaderBar.style.width = '100%';
      if (preloaderText) preloaderText.textContent = 'System Ready!';
      
      setTimeout(() => {
        if (preloader) preloader.classList.add('fade-out');
        initScrollObservers();
      }, 450);
    } else {
      if (preloaderBar) preloaderBar.style.width = progress + '%';
      for (let i = stages.length - 1; i >= 0; i--) {
        if (progress >= stages[i].at) {
          if (preloaderText) preloaderText.textContent = stages[i].text;
          break;
        }
      }
    }
  }, 75);

  /* ------------------------------------------------------------------------
     2. INTERACTIVE PARTICLE CANVAS BACKGROUND
     ------------------------------------------------------------------------ */
  const canvas = document.getElementById('particle-canvas');
  if (canvas) {
    const ctx = canvas.getContext('2d');
    let particlesArray = [];
    let mouse = { x: null, y: null, radius: 140 };

    function resizeCanvas() {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    }
    resizeCanvas();
    window.addEventListener('resize', () => {
      resizeCanvas();
      initParticles();
    });

    window.addEventListener('mousemove', (e) => {
      mouse.x = e.x;
      mouse.y = e.y;
      
      const spotlight = document.getElementById('mouseSpotlight');
      if (spotlight) {
        spotlight.style.transform = `translate(${e.clientX}px, ${e.clientY}px)`;
      }
    });

    class Particle {
      constructor() {
        this.x = Math.random() * canvas.width;
        this.y = Math.random() * canvas.height;
        this.size = Math.random() * 2 + 1;
        this.speedX = (Math.random() - 0.5) * 0.6;
        this.speedY = (Math.random() - 0.5) * 0.6;
        this.color = Math.random() > 0.5 ? 'rgba(0, 119, 238, 0.35)' : 'rgba(0, 212, 255, 0.35)';
      }

      update() {
        this.x += this.speedX;
        this.y += this.speedY;

        if (this.x > canvas.width) this.x = 0;
        else if (this.x < 0) this.x = canvas.width;
        if (this.y > canvas.height) this.y = 0;
        else if (this.y < 0) this.y = canvas.height;
      }

      draw() {
        ctx.fillStyle = this.color;
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.fill();
      }
    }

    function initParticles() {
      particlesArray = [];
      const numberOfParticles = Math.floor((canvas.width * canvas.height) / 22000);
      for (let i = 0; i < numberOfParticles; i++) {
        particlesArray.push(new Particle());
      }
    }
    initParticles();

    function connectParticles() {
      for (let a = 0; a < particlesArray.length; a++) {
        for (let b = a; b < particlesArray.length; b++) {
          const dx = particlesArray[a].x - particlesArray[b].x;
          const dy = particlesArray[a].y - particlesArray[b].y;
          const distance = Math.sqrt(dx * dx + dy * dy);

          if (distance < 110) {
            const opacity = (1 - distance / 110) * 0.2;
            ctx.strokeStyle = `rgba(0, 119, 238, ${opacity})`;
            ctx.lineWidth = 1;
            ctx.beginPath();
            ctx.moveTo(particlesArray[a].x, particlesArray[a].y);
            ctx.lineTo(particlesArray[b].x, particlesArray[b].y);
            ctx.stroke();
          }
        }
      }
    }

    function animateParticles() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      for (let i = 0; i < particlesArray.length; i++) {
        particlesArray[i].update();
        particlesArray[i].draw();
      }
      connectParticles();
      requestAnimationFrame(animateParticles);
    }
    animateParticles();
  }

  /* ------------------------------------------------------------------------
     3. CUSTOM DESKTOP CURSOR (SMOOTH LERP)
     ------------------------------------------------------------------------ */
  const cursorDot = document.getElementById('cursorDot');
  const cursorRing = document.getElementById('cursorRing');

  let mouseX = 0, mouseY = 0;
  let ringX = 0, ringY = 0;
  const isTouchDevice = ('ontouchstart' in window) || (navigator.maxTouchPoints > 0);

  if (!isTouchDevice && cursorDot && cursorRing) {
    document.addEventListener('mousemove', (e) => {
      mouseX = e.clientX;
      mouseY = e.clientY;
      cursorDot.style.left = `${mouseX}px`;
      cursorDot.style.top = `${mouseY}px`;
    });

    function renderCursorRing() {
      ringX += (mouseX - ringX) * 0.18;
      ringY += (mouseY - ringY) * 0.18;
      cursorRing.style.left = `${ringX}px`;
      cursorRing.style.top = `${ringY}px`;
      requestAnimationFrame(renderCursorRing);
    }
    renderCursorRing();

    const interactiveElements = document.querySelectorAll('a, button, .rp-card, .product-card, .workflow-step, .stat-item');
    interactiveElements.forEach(el => {
      el.addEventListener('mouseenter', () => document.body.classList.add('hovering-link'));
      el.addEventListener('mouseleave', () => document.body.classList.remove('hovering-link'));
    });
  }

  /* ------------------------------------------------------------------------
     4. TOP SCROLL PROGRESS INDICATOR
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
     5. SCROLL OBSERVERS & REVEAL ANIMATIONS
     ------------------------------------------------------------------------ */
  function initScrollObservers() {
    const revealElements = document.querySelectorAll('.reveal, .rp-card, .product-card, .workflow-step');
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('active');
        }
      });
    }, { threshold: 0.12 });

    revealElements.forEach(el => observer.observe(el));
  }

  /* ------------------------------------------------------------------------
     6. 3D TILT EFFECT ON HERO / VISUAL CARDS
     ------------------------------------------------------------------------ */
  const tiltCards = document.querySelectorAll('.hero-visual-card, #heroTiltCard, .map-container-wrap');
  tiltCards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;
      const rotateX = ((y - centerY) / centerY) * -6;
      const rotateY = ((x - centerX) / centerX) * 6;

      card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.01, 1.01, 1.01)`;
    });

    card.addEventListener('mouseleave', () => {
      card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)';
    });
  });

  /* ------------------------------------------------------------------------
     7. STICKY NAVBAR & BACK TO TOP BUTTON
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
     8. QUICK ENQUIRY MODAL POPULATOR
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
