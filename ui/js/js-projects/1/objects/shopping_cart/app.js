//Shopping Cart → add/remove items, calculate total.

const shopping_cart = () =>{
    let cart = [] //carts will be added here

    //adding a pen to it
    cart.push({
        name:"pen",
        brand:"matador",
        year:2025
    })

    //adding a book to it
    cart.push({
        name:"js book",
        author:"jhankar",
        year:2025
    })

    //checking cart items
    console.log(cart);

    let total = cart.length;
    console.log(`total items in cart: ${total}`);
}

shopping_cart()