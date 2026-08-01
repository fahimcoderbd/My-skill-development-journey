//nullish operator

let userName = null;
let default_name = "Fahim";
let result = default_name ?? userName;
console.log(result); // return default_name cause userName = null