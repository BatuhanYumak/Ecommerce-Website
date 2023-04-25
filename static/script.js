
function toggleDropdown() {
    var dropdown = document.getElementById("dropdown");
    if (dropdown.style.display === "none") {
      dropdown.style.display = "block";
    } else {
      dropdown.style.display = "none";
    }
  }


  // Define an empty shopping cart object
let cart = {};

// Get all the "Add to Cart" buttons on the page
const addToCartButtons = document.querySelectorAll('.add-to-cart');

// Add an event listener to each button
addToCartButtons.forEach(button => {
  button.addEventListener('click', (event) => {
    // Get the product information from the button's data attributes
    const productName = event.target.dataset.productName;
    const productImage = event.target.parentElement.querySelector('img').src;
    const productPrice = 100; // Replace with actual price

    // Add the product to the cart object
    if (cart[productName]) {
      cart[productName].quantity++;
    } else {
      cart[productName] = {
        image: productImage,
        price: productPrice,
        quantity: 1
      };
    }
  });
});
    // Update 