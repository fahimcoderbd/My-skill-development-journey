// Problem 1: Change paragraph text
const chnage_text = () => {
    let p = document.getElementById('text');
    p.innerText = "JavaScript is awesome!";
}

// Problem 2: Add innerHTML content
const magic = () => {
    let div = document.getElementById('content');
    div.innerHTML += `
        <h2>Hello</h2>
        <p>This is from innerHTML</p>
    `;
}

// Problem 3: Change first element with querySelector
const chnage_first_text = () => {
    let first = document.querySelector('.line');
    first.innerText = "Changed First Line";
}

// Problem 4: Replace multiple elements with querySelectorAll
const replace_fruits = () => {
    let fruits = document.querySelectorAll('.fruits');
    let texts = ["Mango", "Banana", "Orange"];
    fruits.forEach((fruit, index) => {
        fruit.innerText = texts[index];
    });
}
