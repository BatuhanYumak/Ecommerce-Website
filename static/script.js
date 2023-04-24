
function toggleDropdown() {
    var dropdown = document.getElementById("dropdown");
    if (dropdown.style.display === "none") {
      dropdown.style.display = "block";
    } else {
      dropdown.style.display = "none";
    }
  }let cartItems = [];

function toggleCart() {
  const cartDropdown = document.getElementById("cart-dropdown");
  cartDropdown.style.display = cartDropdown.style.display === "none" ? "block" : "none";
}

function addItemToCart(item) {
  // Check if item is already in cart
  for (let i = 0; i < cartItems.length; i++) {
    if (cartItems[i].id === item.id) {
      cartItems[i].quantity++;
      updateCart();
      return;
    }
  }

  // If item is not in cart, add it
  cartItems.push({
    id: item.id,
    name: item.name,
    price: item.price,
    quantity: 1
  });

  updateCart();
}

function updateCart() {
  const cartCount = document.querySelector(".cart-count");
  const cartItemsList = document.getElementById("cart-items");
  const cartTotalPrice = document.getElementById("cart-total-price");
  let total = 0;
  let count = 0;

  // Update cart count
  cartCount.innerHTML = cartItems.reduce((acc, item) => {
    return acc + item.quantity;
  }, 0);

  // Update cart items
  cartItems.forEach(item => {
    const listItem = document.createElement("li");
    listItem.innerHTML = `${item.quantity}x ${item.name} - $${item.price * item.quantity}`;
    cartItemsList.appendChild(listItem);
    total += item.price * item.quantity;
    count += item.quantity;
  });

  // Update cart total price
  cartTotalPrice.innerHTML = `$${total.toFixed(2)}`;

  // Update cart empty message
  const cartEmptyMessage = document.getElementById("cart-empty-message");
  cartEmptyMessage.style.display = cartItems.length === 0 ? "block" : "none";
}
