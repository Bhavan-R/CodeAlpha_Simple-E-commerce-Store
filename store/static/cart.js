// Product-ah cart-la add panna
function addToCart(id, name, price) {
    let cart = JSON.parse(localStorage.getItem('my_cart')) || [];
    cart.push({ id: id, name: name, price: price });
    localStorage.setItem('my_cart', JSON.stringify(cart));
    alert(name + " added to cart!");
}

// Cart page-la items-ah kaata
function displayCart() {
    let cart = JSON.parse(localStorage.getItem('my_cart')) || [];
    let cartList = document.getElementById('cart-list');
    if (cartList) {
        if (cart.length === 0) {
            cartList.innerHTML = "<p>Your cart is empty.</p>";
        } else {
            cartList.innerHTML = cart.map(item => `<li>${item.name} - $${item.price}</li>`).join('');
        }
    }
}