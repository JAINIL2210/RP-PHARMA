/**
 * RP PHARMA — Admin Portal Script
 */

document.addEventListener('DOMContentLoaded', () => {
  // Sidebar toggle on mobile
  const sidebarToggle = document.getElementById('sidebarToggle');
  const sidebar = document.querySelector('.admin-sidebar');

  if (sidebarToggle && sidebar) {
    sidebarToggle.addEventListener('click', () => {
      sidebar.classList.toggle('show');
    });
  }

  // Delete confirmation
  const deleteForms = document.querySelectorAll('.form-delete-confirm');
  deleteForms.forEach(form => {
    form.addEventListener('submit', (e) => {
      if (!confirm('Are you sure you want to permanently delete this item? This action cannot be undone.')) {
        e.preventDefault();
      }
    });
  });
});
