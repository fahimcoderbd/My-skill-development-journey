//dom (document object model)
//feature:grab html elements 
//so we can chnage them using js

//getElementbyId --used for getting elements's id
let myname = document.getElementById('myname')
console.log(myname); //it will print my name

//let's change a item
const change = () =>{
    let name = document.getElementById('myname')
    name.innerText = "Text chnaged";

    //query selector
    let color = document.querySelector('.text'); 
    color.style.color = 'red'; //change text color
}
