let input = document.getElementById('input');
let p = document.getElementById('show');

// live update
input.addEventListener("keyup", () => {
    p.innerText = input.value;
});

//problem 6 solution
let input2 = document.getElementById('input2');
let p2 = document.getElementById('show2');

input2.addEventListener("keyup", () =>{
    p2.innerHTML = `
    <b>${input2.value}</b>
    `
})

//toogle text

let p3 = document.getElementById("content");
let btn = document.getElementById("btn");

btn.addEventListener("click", () => {
    if (p3.innerText === "Hello World") {
        p3.innerText = "Goodbye World";
    } else {
        p3.innerText = "Hello World";
    }
});

//problem 8
 function change_text() {
      // get all elements with class "msg"
      let elements = document.getElementsByClassName("msg");

      // loop through all and change text
      for (let i = 0; i < elements.length; i++) {
        elements[i].innerText = "Fahim Abrar"; // 👉 put your name
      }
    }