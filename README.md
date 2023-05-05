# Django Ecommerce Group Project

## Installation

-   Create a virtual enviornment and activate it
-   Clone the project

Type below command to install npm+pip packages

```
npm run setup
```

Start Vite

```
npm run dev
```

Start Django

```
npm run server
```

Navigate to **127.0.0.1:8000** in browser

<br>

To build for production (all files will be in static/dist)

```
npm run build
```

Project structure

## app:

Universal app features, that don't fit into the other apps. Like loading universal templates or a global context processer.

## products:

This app is responsible for managing products and their attributes, such as name, description, price, and image. It typically includes models for products and related objects, such as categories and tags, and views and templates for displaying and searching for products.

## cart:

This app is responsible for managing the user's shopping cart. It typically includes views and templates for adding and removing items from the cart, calculating the total price of the cart, and displaying the contents of the cart.

## checkout:

This app is responsible for managing the checkout process. It typically includes views and templates for collecting shipping and payment information from the user, validating the information, and creating an order.

## orders:

This app is responsible for managing orders and their status. It typically includes models for orders and related objects, such as order items and shipping information, and views and templates for displaying and updating order status.

## users:

This app is responsible for managing user authentication and profiles. It typically includes views and templates for user registration, login, and logout, as well as models for user profiles and related objects, such as addresses and payment methods.
