//let vs var
//let -we can can't access blocked variable from outside
//var -can be accessed from anywhere in codebase

my_name = "Fahim"

//let code
if (my_name == "Fahim"){
    let response = true;
    console.log("Response from 1: ",response);
}

//var code
if (my_name == "Fahim"){
    var response2 = true;
    console.log("Response from 2",response2)
}

//accesing var's variable from outside
console.log("From outside: ",response2)