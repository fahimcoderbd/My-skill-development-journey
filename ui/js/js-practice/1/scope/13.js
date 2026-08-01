// Block scoped variables
// Can't be accessed outside of the blocks
// let and const are used

// Block scope
// For accessing the block scoped variable 
let output;

const isLoggedin = true; // true

if (isLoggedin === true) {
    const show_msg = "You logged in successfully!"; // message to user
    console.log(show_msg);
    //assigning outside 
    output = show_msg
}

console.log(output);

console.log(isLoggedin);