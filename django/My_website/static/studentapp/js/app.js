/**
 * Student App - Modern JavaScript Utility
 * Handles form validation, confirmations, and user interactions
 */

document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
});

function initializeApp() {
    // Initialize form validation
    initializeFormValidation();
    
    // Initialize delete confirmations
    initializeDeleteConfirmations();
    
    // Initialize smooth animations
    initializeSmoothAnimations();
}

/**
 * Form Validation
 */
function initializeFormValidation() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!validateForm(this)) {
                e.preventDefault();
            }
        });
    });

    // Real-time validation for inputs
    const inputs = document.querySelectorAll('input[type="text"], input[type="email"], input[type="number"]');
    inputs.forEach(input => {
        input.addEventListener('blur', function() {
            validateField(this);
        });
    });
}

function validateForm(form) {
    let isValid = true;
    const fields = form.querySelectorAll('[required]');

    fields.forEach(field => {
        if (!validateField(field)) {
            isValid = false;
        }
    });

    return isValid;
}

function validateField(field) {
    const value = field.value.trim();
    let isValid = true;

    // Check if field is empty
    if (field.hasAttribute('required') && !value) {
        showFieldError(field, 'This field is required');
        return false;
    }

    // Email validation
    if (field.type === 'email' && value) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(value)) {
            showFieldError(field, 'Please enter a valid email address');
            return false;
        }
    }

    // Number validation
    if (field.type === 'number' && value) {
        const min = field.getAttribute('min');
        const max = field.getAttribute('max');

        if (min && parseInt(value) < parseInt(min)) {
            showFieldError(field, `Minimum value is ${min}`);
            return false;
        }

        if (max && parseInt(value) > parseInt(max)) {
            showFieldError(field, `Maximum value is ${max}`);
            return false;
        }
    }

    // Min length validation
    if (field.type === 'text' && value) {
        const minLength = field.getAttribute('minlength');
        if (minLength && value.length < parseInt(minLength)) {
            showFieldError(field, `Minimum length is ${minLength} characters`);
            return false;
        }
    }

    // Clear error if validation passes
    clearFieldError(field);
    return true;
}

function showFieldError(field, message) {
    clearFieldError(field);
    
    field.style.borderColor = 'var(--danger-color)';
    field.style.boxShadow = '0 0 0 3px rgba(239, 68, 68, 0.1)';
    
    const errorElement = document.createElement('small');
    errorElement.className = 'field-error';
    errorElement.style.color = 'var(--danger-color)';
    errorElement.style.display = 'block';
    errorElement.style.marginTop = '0.25rem';
    errorElement.textContent = message;
    
    field.parentNode.insertBefore(errorElement, field.nextSibling);
}

function clearFieldError(field) {
    const errorElement = field.nextElementSibling;
    if (errorElement && errorElement.classList.contains('field-error')) {
        errorElement.remove();
    }
    
    field.style.borderColor = '';
    field.style.boxShadow = '';
}

/**
 * Delete Confirmations
 */
function initializeDeleteConfirmations() {
    const deleteButtons = document.querySelectorAll('a[class*="btn-danger"]');
    
    deleteButtons.forEach(button => {
        if (button.href.includes('delete')) {
            button.addEventListener('click', function(e) {
                if (!confirmDelete(this)) {
                    e.preventDefault();
                }
            });
        }
    });
}

function confirmDelete(element) {
    const studentName = element.closest('tr')?.querySelector('td.font-bold')?.textContent || 'this student';
    const message = `Are you absolutely sure you want to delete ${studentName}? This action cannot be undone.`;
    
    return confirm(message);
}

/**
 * Smooth Animations
 */
function initializeSmoothAnimations() {
    // Add animation to alerts
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        alert.style.animation = 'slideIn 0.3s ease';
    });

    // Add hover effects to cards
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
}

/**
 * Utility Functions
 */

/**
 * Show success toast notification
 */
function showSuccess(message, duration = 3000) {
    showToast(message, 'success', duration);
}

/**
 * Show error toast notification
 */
function showError(message, duration = 3000) {
    showToast(message, 'danger', duration);
}

/**
 * Show toast notification
 */
function showToast(message, type = 'info', duration = 3000) {
    const toast = document.createElement('div');
    toast.className = `alert alert-${type}`;
    toast.textContent = message;
    toast.style.position = 'fixed';
    toast.style.top = '20px';
    toast.style.right = '20px';
    toast.style.zIndex = '9999';
    toast.style.maxWidth = '400px';
    toast.style.animation = 'slideIn 0.3s ease';

    document.body.appendChild(toast);

    setTimeout(() => {
        toast.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => toast.remove(), 300);
    }, duration);
}

/**
 * Format date to readable format
 */
function formatDate(date) {
    return new Date(date).toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    });
}

/**
 * Debounce function for search/filter
 */
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

/**
 * Export functions for use in templates
 */
window.StudentApp = {
    showSuccess,
    showError,
    showToast,
    formatDate,
    validateForm,
    validateField,
    confirmDelete
};