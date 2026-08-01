//destructuring js

/*  i can fetch values from arrays and objects  
 then set their values into variables directly  */
/* let arr = [3,5,8,9,10]
let [a, , , , ...rest] = arr
console.log(a ,rest); */

//spread operator
let arr1 = [1,2,3]
let obj = {...arr1}
console.log(obj);

function sum(v1,v2,v3){
    return v1 + v2 + v3;
}

let result  = sum(...arr1);
console.log(result);


let obj2 = {
  name:"fahim",
  company:"xyz",
  address:"xyz"
}

console.log({name:"john" ,...obj2 });