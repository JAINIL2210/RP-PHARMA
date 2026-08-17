/**
 * RP PHARMA — Product Catalogue Search & Filter Script
 */

document.addEventListener('DOMContentLoaded', () => {
  const searchInput = document.getElementById('productSearchInput');
  const productCards = document.querySelectorAll('.product-grid-item');
  const resultsCount = document.getElementById('resultsCount');
  const noResultsMsg = document.getElementById('noResultsMessage');
  const filterTypeRadios = document.querySelectorAll('input[name="filterType"]');
  const filterCategorySelect = document.getElementById('filterCategorySelect');
  const filterDosageSelect = document.getElementById('filterDosageSelect');
  const resetBtn = document.getElementById('resetFiltersBtn');

  if (!productCards.length) return;

  function filterCatalog() {
    const searchTerm = searchInput ? searchInput.value.toLowerCase().trim() : '';
    
    let selectedType = 'all';
    filterTypeRadios.forEach(radio => {
      if (radio.checked) selectedType = radio.value;
    });

    const selectedCategory = filterCategorySelect ? filterCategorySelect.value.toLowerCase() : '';
    const selectedDosage = filterDosageSelect ? filterDosageSelect.value.toLowerCase() : '';

    let visibleCount = 0;

    productCards.forEach(card => {
      const name = (card.getAttribute('data-name') || '').toLowerCase();
      const composition = (card.getAttribute('data-composition') || '').toLowerCase();
      const type = (card.getAttribute('data-type') || '').toLowerCase();
      const category = (card.getAttribute('data-category') || '').toLowerCase();
      const dosage = (card.getAttribute('data-dosage') || '').toLowerCase();
      const indications = (card.getAttribute('data-indications') || '').toLowerCase();

      // Check matches
      const matchesSearch = !searchTerm || 
                            name.includes(searchTerm) || 
                            composition.includes(searchTerm) || 
                            indications.includes(searchTerm) ||
                            dosage.includes(searchTerm);

      const matchesType = (selectedType === 'all') || (type === selectedType);
      const matchesCategory = !selectedCategory || (category === selectedCategory);
      const matchesDosage = !selectedDosage || (dosage.includes(selectedDosage));

      if (matchesSearch && matchesType && matchesCategory && matchesDosage) {
        card.style.display = 'block';
        visibleCount++;
      } else {
        card.style.display = 'none';
      }
    });

    if (resultsCount) {
      resultsCount.textContent = visibleCount;
    }

    if (noResultsMsg) {
      noResultsMsg.style.display = visibleCount === 0 ? 'block' : 'none';
    }
  }

  // Debounced search
  let debounceTimeout;
  if (searchInput) {
    searchInput.addEventListener('input', () => {
      clearTimeout(debounceTimeout);
      debounceTimeout = setTimeout(filterCatalog, 150);
    });
  }

  // Filter change listeners
  filterTypeRadios.forEach(radio => {
    radio.addEventListener('change', filterCatalog);
  });

  if (filterCategorySelect) {
    filterCategorySelect.addEventListener('change', filterCatalog);
  }

  if (filterDosageSelect) {
    filterDosageSelect.addEventListener('change', filterCatalog);
  }

  // Reset Filters button
  if (resetBtn) {
    resetBtn.addEventListener('click', (e) => {
      e.preventDefault();
      if (searchInput) searchInput.value = '';
      const allTypeRadio = document.querySelector('input[name="filterType"][value="all"]');
      if (allTypeRadio) allTypeRadio.checked = true;
      if (filterCategorySelect) filterCategorySelect.value = '';
      if (filterDosageSelect) filterDosageSelect.value = '';
      filterCatalog();
    });
  }

  // Initial filter run on page load
  filterCatalog();
});
