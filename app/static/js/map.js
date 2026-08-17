/**
 * RP PHARMA — Global Presence Interactive Map Visualization
 */

document.addEventListener('DOMContentLoaded', () => {
  const regionCards = document.querySelectorAll('.map-region-card');
  const regionBadge = document.getElementById('activeRegionName');
  const regionDesc = document.getElementById('activeRegionDesc');

  const regionDetails = {
    'asia': {
      name: 'Southeast & South Asia',
      desc: 'Active partner distribution network delivering essential antibiotic, cardiovascular, and nutraceutical formulations with full regulatory dossiers.'
    },
    'africa': {
      name: 'Africa (Sub-Saharan & North)',
      desc: 'Supplying institutional healthcare programs and established commercial distributors with WHO-GMP compliant formulations and stability data.'
    },
    'middle-east': {
      name: 'Middle East & GCC',
      desc: 'Partnering with licensed regional distributors for specialized formulations and premium nutraceutical supplements.'
    },
    'cis': {
      name: 'CIS & Eastern European Corridor',
      desc: 'CTD-formatted technical documentation and product dossiers tailored for regional drug regulatory authorities.'
    },
    'latam': {
      name: 'Latin America',
      desc: 'Expanding presence with key pharmaceutical importers and tender supply partners in Central and South American markets.'
    }
  };

  regionCards.forEach(card => {
    card.addEventListener('mouseenter', () => {
      const regionKey = card.getAttribute('data-region');
      if (regionDetails[regionKey]) {
        if (regionBadge) regionBadge.textContent = regionDetails[regionKey].name;
        if (regionDesc) regionDesc.textContent = regionDetails[regionKey].desc;
      }
    });
  });
});
