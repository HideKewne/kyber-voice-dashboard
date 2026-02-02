/**
 * Kyber Dashboard - JavaScript
 * Handles interactivity for both Brand and White themes
 */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all components
    initDropdowns();
    initSidebar();
    initSearch();
    initNotifications();
    initProgressRings();
});

/**
 * Dropdown Menu Handler
 */
function initDropdowns() {
    const dropdowns = document.querySelectorAll('.dropdown');

    dropdowns.forEach(dropdown => {
        const toggle = dropdown.querySelector('.dropdown-toggle, .user-dropdown-btn');
        const menu = dropdown.querySelector('.dropdown-menu');

        if (toggle && menu) {
            toggle.addEventListener('click', (e) => {
                e.stopPropagation();
                dropdown.classList.toggle('open');

                // Close other dropdowns
                dropdowns.forEach(other => {
                    if (other !== dropdown) {
                        other.classList.remove('open');
                    }
                });
            });
        }
    });

    // Close dropdowns when clicking outside
    document.addEventListener('click', () => {
        dropdowns.forEach(dropdown => {
            dropdown.classList.remove('open');
        });
    });
}

/**
 * Sidebar Mobile Toggle
 */
function initSidebar() {
    const sidebar = document.querySelector('.sidebar');
    const mainContent = document.querySelector('.main-content');

    // Create mobile menu button if it doesn't exist
    let mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    if (!mobileMenuBtn && window.innerWidth <= 768) {
        mobileMenuBtn = document.createElement('button');
        mobileMenuBtn.className = 'mobile-menu-btn';
        mobileMenuBtn.innerHTML = `
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <line x1="3" y1="12" x2="21" y2="12"/>
                <line x1="3" y1="6" x2="21" y2="6"/>
                <line x1="3" y1="18" x2="21" y2="18"/>
            </svg>
        `;
        mobileMenuBtn.style.cssText = `
            position: fixed;
            top: 16px;
            left: 16px;
            z-index: 200;
            width: 40px;
            height: 40px;
            background: var(--glass-bg, rgba(255,255,255,0.9));
            border: 1px solid var(--glass-border, #e4e4e7);
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
        `;
        mobileMenuBtn.querySelector('svg').style.cssText = 'width: 20px; height: 20px;';
        document.body.appendChild(mobileMenuBtn);

        mobileMenuBtn.addEventListener('click', () => {
            sidebar.classList.toggle('open');
        });

        // Close sidebar when clicking on main content
        mainContent.addEventListener('click', () => {
            if (sidebar.classList.contains('open')) {
                sidebar.classList.remove('open');
            }
        });
    }

    // Handle sidebar navigation
    const navItems = document.querySelectorAll('.nav-item');
    navItems.forEach(item => {
        item.addEventListener('click', (e) => {
            // Remove active class from all items
            navItems.forEach(nav => nav.classList.remove('active'));
            // Add active class to clicked item
            item.classList.add('active');

            // Close sidebar on mobile after selection
            if (window.innerWidth <= 768) {
                sidebar.classList.remove('open');
            }
        });
    });
}

/**
 * Search Functionality
 */
function initSearch() {
    const searchBar = document.querySelector('.search-bar input');

    if (searchBar) {
        searchBar.addEventListener('focus', () => {
            searchBar.parentElement.classList.add('focused');
        });

        searchBar.addEventListener('blur', () => {
            searchBar.parentElement.classList.remove('focused');
        });

        searchBar.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                e.preventDefault();
                const query = searchBar.value.trim();
                if (query) {
                    handleSearch(query);
                }
            }
        });
    }
}

function handleSearch(query) {
    console.log('Searching for:', query);
    // Implement search functionality here
    // This would typically make an API call to search the knowledge base
}

/**
 * Notifications
 */
function initNotifications() {
    const notificationBtn = document.querySelector('.notification-btn');

    if (notificationBtn) {
        notificationBtn.addEventListener('click', () => {
            // Toggle notification panel
            console.log('Toggle notifications');
            // Implement notification panel here
        });
    }
}

/**
 * Animate Progress Rings
 */
function initProgressRings() {
    const progressRings = document.querySelectorAll('.progress-ring-fill');

    progressRings.forEach(ring => {
        const circumference = 2 * Math.PI * 40; // radius = 40
        const offset = ring.getAttribute('stroke-dashoffset');

        // Animate from full offset to target offset
        ring.style.strokeDashoffset = circumference;

        setTimeout(() => {
            ring.style.transition = 'stroke-dashoffset 1s ease-out';
            ring.style.strokeDashoffset = offset;
        }, 100);
    });
}

/**
 * Action Button Handlers
 */
document.querySelectorAll('.action-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        const action = btn.textContent.trim();
        console.log('Action clicked:', action);

        switch (action) {
            case 'New Client Onboarding':
            case 'Add Client':
                showModal('Add New Client');
                break;
            case 'Schedule Interview':
            case 'New Interview':
                showModal('Schedule Interview');
                break;
            case 'Add Knowledge Entry':
            case 'Update Knowledge':
                showModal('Add Knowledge Entry');
                break;
            case 'Generate Report':
                showModal('Generate Report');
                break;
        }
    });
});

/**
 * Modal Handler (placeholder)
 */
function showModal(title) {
    console.log('Opening modal:', title);
    // Implement modal functionality here
    alert(`${title} - Coming soon!`);
}

/**
 * Activity Item Handlers
 */
document.querySelectorAll('.activity-item').forEach(item => {
    item.addEventListener('click', () => {
        const text = item.querySelector('.activity-text').textContent;
        console.log('Activity clicked:', text);
        // Navigate to relevant section
    });
});

/**
 * Responsive Handler
 */
window.addEventListener('resize', () => {
    const sidebar = document.querySelector('.sidebar');
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');

    if (window.innerWidth > 768) {
        sidebar.classList.remove('open');
        if (mobileMenuBtn) {
            mobileMenuBtn.style.display = 'none';
        }
    } else {
        if (mobileMenuBtn) {
            mobileMenuBtn.style.display = 'flex';
        }
    }
});

/**
 * Keyboard Shortcuts
 */
document.addEventListener('keydown', (e) => {
    // Cmd/Ctrl + K for search
    if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
        e.preventDefault();
        const searchBar = document.querySelector('.search-bar input');
        if (searchBar) {
            searchBar.focus();
        }
    }

    // Escape to close modals/dropdowns
    if (e.key === 'Escape') {
        document.querySelectorAll('.dropdown.open').forEach(dropdown => {
            dropdown.classList.remove('open');
        });
        document.querySelector('.sidebar')?.classList.remove('open');
    }
});
