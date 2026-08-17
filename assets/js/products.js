/**
 * RP PHARMA — Product Catalogue Filter & Search Script
 */

document.addEventListener('DOMContentLoaded', () => {
  const searchInput = document.getElementById('productSearchInput');
  const typeRadios = document.querySelectorAll('input[name="filterType"]');
  const categorySelect = document.getElementById('filterCategorySelect');
  const dosageSelect = document.getElementById('filterDosageSelect');
  const resetBtn = document.getElementById('resetFiltersBtn');
  const productItems = document.querySelectorAll('.product-grid-item');
  const resultsCount = document.getElementById('resultsCount');
  const noResults = document.getElementById('noResultsMessage');

  function filterProducts() {
    const searchTerm = (searchInput ? searchInput.value.toLowerCase().trim() : '');
    
    let selectedType = 'all';
    typeRadios.forEach(radio => {
      if (radio.checked) selectedType = radio.value;
    });

    const selectedCategory = (categorySelect ? categorySelect.value.toLowerCase() : '');
    const selectedDosage = (dosageSelect ? dosageSelect.value.toLowerCase() : '');

    let visibleCount = 0;

    productItems.forEach(item => {
      const name = (item.dataset.name || '').toLowerCase();
      const composition = (item.dataset.composition || '').toLowerCase();
      const type = (item.dataset.type || '').toLowerCase();
      const category = (item.dataset.category || '').toLowerCase();
      const dosage = (item.dataset.dosage || '').toLowerCase();
      const indications = (item.dataset.indications || '').toLowerCase();

      // Type match
      const typeMatch = (selectedType === 'all' || type === selectedType);

      // Category match
      const categoryMatch = (!selectedCategory || category === selectedCategory);

      // Dosage match
      const dosageMatch = (!selectedDosage || dosage.includes(selectedDosage));

      // Search match
      const searchMatch = (!searchTerm ||
        name.includes(searchTerm) ||
        composition.includes(searchTerm) ||
        indications.includes(searchTerm) ||
        dosage.includes(searchTerm)
      );

      if (typeMatch && categoryMatch && dosageMatch && searchMatch) {
        item.style.display = 'block';
        visibleCount++;
      } else {
        item.style.display = 'none';
      }
    });

    if (resultsCount) {
      resultsCount.textContent = visibleCount;
    }

    if (noResults) {
      noResults.style.display = (visibleCount === 0) ? 'block' : 'none';
    }
  }

  // Event Listeners
  if (searchInput) {
    searchInput.addEventListener('input', filterProducts);
  }

  typeRadios.forEach(radio => {
    radio.addEventListener('change', filterProducts);
  });

  if (categorySelect) {
    categorySelect.addEventListener('change', filterProducts);
  }

  if (dosageSelect) {
    dosageSelect.addEventListener('change', filterProducts);
  }

  if (resetBtn) {
    resetBtn.addEventListener('click', (e) => {
      e.preventDefault();
      if (searchInput) searchInput.value = '';
      const allRadio = document.getElementById('typeAll');
      if (allRadio) allRadio.checked = true;
      if (categorySelect) categorySelect.value = '';
      if (dosageSelect) dosageSelect.value = '';
      filterProducts();
    });
  }

  // Initial Filter pass
  filterProducts();
});
