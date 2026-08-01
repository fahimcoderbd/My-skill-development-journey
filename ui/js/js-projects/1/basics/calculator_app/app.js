//simple calculator app

//taking number 1
const num1 = Number(prompt("Enter number 1: "));
//taking number 2
const num2 = Number(prompt("Enter number 2: "));

const op = prompt("Select an operator (1)plus (2)minus: ")

const result = (n1, n2, o) => {
    if (isNaN(n1) || isNaN(n2)) {
        alert("Please enter valid numbers.");
        return;
    }
    if (o == "1") {
        alert("Your result is: " + (n1 + n2));
    } else if (o == "2") {
        alert("Your result is: " + (n1 - n2));
    } else {
        alert("Something went wrong, Try again");
    }
}

result(num1, num2, op);