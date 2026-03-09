// Function to calculate total for a row
function calculateTotal(row) {
    const quantityInput = row.querySelector('input[name="quantity"]');
    const priceInput = row.querySelector('input[name="price"]');
    const totalDisplay = row.querySelector('.total-display');
    const totalInput = row.querySelector('input[name="total"]');

    if (quantityInput && priceInput && totalDisplay && totalInput) {
        const quantity = parseFloat(quantityInput.value) || 0;
        const price = parseFloat(priceInput.value) || 0;
        const total = quantity * price;
        totalDisplay.textContent = total.toFixed(2);
        totalInput.value = total.toFixed(2);
    }
}

// Function to attach event listeners to quantity and price inputs
function attachCalculationListeners() {
    const table = document.querySelector('.invoice-table');
    if (table) {
        table.addEventListener('input', function(event) {
            const target = event.target;
            if (target.name === 'quantity' || target.name === 'price') {
                const row = target.closest('tr');
                calculateTotal(row);
            }
        });
    }
}

// Function to add a new item row
function addItem() {
    const table = document.querySelector('.invoice-table');
    if (table) {
        const newRow = document.createElement('tr');
        newRow.className = 'table-details';
        newRow.innerHTML = `
            <td><input type="text" name="invoice_itemdescription" required class="invoice-table-description" placeholder="Enter item description"></td>
            <td><input type="number" name="quantity" required></td>
            <td><input type="number" step="0.01" name="price" required></td>
            <td><span class="total-display"></span><input type="hidden" name="total" required></td>
            <td><button type="button" onclick="removeItem(this)">Remove</button></td>
        `;
        table.appendChild(newRow);
    }
}

// Function to remove an item row
function removeItem(button) {
    const row = button.closest('tr');
    if (row) {
        row.remove();
    }
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    attachCalculationListeners();
    // Calculate for existing rows
    const existingRows = document.querySelectorAll('.invoice-table .table-details');
    existingRows.forEach(calculateTotal);
});
