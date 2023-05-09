let cart_items = JSON.parse(localStorage.getItem("cart_items")) || [];

const cart_form = document.querySelector(".cart-add-form");
const cart_add = document.querySelector(".cart-add-form button[auth='true']");


if (cart_add) {
    cart_form.addEventListener("submit", cartAdd);
}

function cartAdd(e) {
    e.preventDefault();
    const quantity = cart_form.querySelector("input[name='input_quantity']").value;
    const product_id = cart_form.querySelector("button[name='product_id']").value;

    let is_product_in_cart = false;
    cart_items.forEach(item => {
      if (item.product_id === product_id) {
        item.quantity = Number(item.quantity) + 1;
        is_product_in_cart = true;
      }
    });

    console.log(cart_items);

    if (!is_product_in_cart) {
        cart_items.push({ product_id: product_id, quantity: quantity });
    };

    localStorage.setItem("cart_items", JSON.stringify(cart_items));
    document.cookie = `cart_items=${encodeURIComponent(cart_items)}`;

    // window.location.href = "/cart";
    console.log(cart_items);
}


function cartRemove(e) {
    e.preventDefault();

    localStorage.setItem("cart_items", JSON.stringify(cart_items));
    document.cookie = `cart_items=${encodeURIComponent(cart_items)}`;

    window.location.href = "/cart";
    console.log(cart_items);
}

function getTotalItems() {
    const cart_items = localStorage.getItem("cart_items");
    if (cart_items) {
        let quantity = 0;
        cart_items.forEach(item => {
            quantity += item.quantity;
        })
        return quantity;
    }
}

document.addEventListener("DOMContentLoaded", function() {
    const cart_items = localStorage.getItem("cart_items");
    if (cart_items) {
        document.cookie = `cart_items=${encodeURIComponent(cart_items)}`;
    }
});