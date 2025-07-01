// Initialize Lucide icons
lucide.createIcons();

// Sample market data
const markets = [
    {
        name: 'Silicon Valley Tech Market',
        lat: 37.7749,
        lng: -122.4194,
        size: 5000000000,
        growth: 12.5
    },
    {
        name: 'London Financial District',
        lat: 51.5074,
        lng: -0.1278,
        size: 3200000000,
        growth: 8.2
    },
    {
        name: 'Tokyo Technology Hub',
        lat: 35.6762,
        lng: 139.6503,
        size: 2800000000,
        growth: 15.8
    },
    {
        name: 'Berlin Startup Ecosystem',
        lat: 52.5200,
        lng: 13.4050,
        size: 1800000000,
        growth: 22.1
    },
    {
        name: 'Singapore FinTech Market',
        lat: 1.3521,
        lng: 103.8198,
        size: 2100000000,
        growth: 18.7
    }
];

// Initialize map
let map;
function initMap() {
    map = L.map('map').setView([20, 0], 2);
    
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    // Add market markers
    markets.forEach(market => {
        const marker = L.marker([market.lat, market.lng])
            .addTo(map)
            .bindPopup(`
                <div class="p-2">
                    <h3 class="font-bold text-lg">${market.name}</h3>
                    <p class="text-sm text-gray-600">Market Size: $${(market.size / 1000000000).toFixed(1)}B</p>
                    <p class="text-sm text-gray-600">Growth Rate: ${market.growth}%</p>
                </div>
            `);
    });
}

// Navigation functionality
function showPage(pageId) {
    // Hide all pages
    document.querySelectorAll('.page').forEach(page => {
        page.classList.add('hidden');
    });
    
    // Show selected page
    document.getElementById(pageId).classList.remove('hidden');
    
    // Update navigation
    document.querySelectorAll('.nav-link').forEach(link => {
        link.classList.remove('active');
    });
    document.querySelector(`[data-page="${pageId}"]`).classList.add('active');
    
    // Initialize map if showing market map page
    if (pageId === 'market-map' && !map) {
        setTimeout(initMap, 100);
    }
}

// Event listeners
window.addEventListener('DOMContentLoaded', function() {
    // Navigation click handlers
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const pageId = this.getAttribute('data-page');
            showPage(pageId);
        });
    });

    // Search functionality
    document.getElementById('search-input').addEventListener('input', function(e) {
        const query = e.target.value.toLowerCase();
        // Filter markets based on search query
        console.log('Searching for:', query);
    });

    // Initialize map on first load
    setTimeout(initMap, 100);
}); 