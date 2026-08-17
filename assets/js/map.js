/**
 * RP PHARMA — Global Markets Interactive Switcher
 */

document.addEventListener('DOMContentLoaded', () => {
  const regionCards = document.querySelectorAll('.map-region-card');
  const activeTitle = document.getElementById('activeRegionName');
  const activeDesc = document.getElementById('activeRegionDesc');

  const regionData = {
    'asia': {
      title: 'Southeast & South Asia',
      desc: 'Active commercial exports across Vietnam, Philippines, Myanmar, Cambodia, and Sri Lanka with dedicated ACTD / CTD dossiers.'
    },
    'africa': {
      title: 'African Continent',
      desc: 'Supplying essential antibiotics, antimalarials, cardiovascular medicines, and multivitamins to distributor networks across 12+ African nations.'
    },
    'middle-east': {
      title: 'Middle East & GCC',
      desc: 'Targeted presence in UAE, Oman, Yemen, and Iraq focusing on premium nutraceutical softgels and finished oral formulations.'
    },
    'cis': {
      title: 'CIS & Central Asia',
      desc: 'Supporting regional healthcare distributors in Uzbekistan, Kazakhstan, and Georgia with high-volume finished formulations.'
    },
    'latam': {
      title: 'Latin America',
      desc: 'Expanding hospital supply and retail pharmacy brand registrations in Central and South American markets.'
    }
  };

  regionCards.forEach(card => {
    card.addEventListener('mouseenter', () => {
      const region = card.getAttribute('data-region');
      if (region && regionData[region] && activeTitle && activeDesc) {
        activeTitle.textContent = regionData[region].title;
        activeDesc.textContent = regionData[region].desc;
      }
    });
  });
});
