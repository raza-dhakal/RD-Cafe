let search = document.querySelector('.search-box');

document.querySelector('#search-icon').onclick = () => {
    search.classList.toggle('active');
    navbar.classList.remove('active');
}

let navbar = document.querySelector('.navbar');

document.querySelector('#menu-icon').onclick = () => {
    navbar.classList.toggle('active');
    navbar.classList.remove('active');
}
window.onscroll = () => {
    navbar.classList.remove('active');
    navbar.classList.remove('active');

}

let header = document.querySelector('header');

window.addEventListener('scroll' , () => {
    header.classList.toggle('shadow', window.scrollY > 0);
});



let cart = [];

function addToCart() {
    const productName = document.getElementById('productName').value;
    const quantity = parseInt(document.getElementById('quantity').value);
    const price = parseFloat(document.getElementById('price').value);

    if (!productName || quantity <= 0 || price <= 0) {
        alert("Please enter valid product details.");
        return;
    }

    const tax = price * 0.03; // 3% tax
    const total = (price + tax) * quantity;
    
    // Add product to cart
    cart.push({ productName, quantity, price, tax, total });
    updateCart();
}

function updateCart() {
    const cartBody = document.getElementById('cartBody');
    cartBody.innerHTML = ""; // Clear the cart table
    
    let totalAmount = 0;
    let totalQuantity = 0;

    cart.forEach(item => {
        const discount = cart.length >= 5 ? item.total * 0.25 : 0; // 25% discount for 5 or more items
        const finalTotal = item.total - discount;

        // Add each product to the cart table
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${item.productName}</td>
            <td>${item.quantity}</td>
            <td>$${item.price.toFixed(2)}</td>
            <td>$${item.tax.toFixed(2)}</td>
            <td>$${discount.toFixed(2)}</td>
            <td>$${finalTotal.toFixed(2)}</td>
        `;
        cartBody.appendChild(row);

        totalAmount += finalTotal;
        totalQuantity += item.quantity;
    });

    // Update total amount in the summary
    document.getElementById('totalAmount').textContent = totalAmount.toFixed(2);
}
