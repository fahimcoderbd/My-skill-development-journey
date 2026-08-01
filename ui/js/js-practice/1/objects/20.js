//problem 1
//1. Create your own object

let studnt = {
    name:"Fahim",
    age:16,
    class:9,
    hobbies:["coding,gaming,book-reading,halal-music,science,robotics,writting,exploring,cycling"]
}

//printing whole object
console.log(studnt);
console.log(studnt["hobbies"])

//problem 2
//add new properties city and grade and print

studnt.city = "Fahim"; //added city
studnt.grade = "f" //added grade
console.log(studnt); //printing object

//3.updating the property
studnt["city"] = "Dhaka";
studnt["grade"] = "a+"
console.log(studnt);

//deleting the property
delete studnt["age"];
console.log(studnt);

//object swith methods
car = {
    brand:"BMW",
    model:"xxx",
    year:2025,
    starting: start = () =>{
        console.log("Car started....");
    },

    stopping: stop = () =>{
         console.log("car stopped!");
    }
}

console.log(car);

//looping through object
let book = {
    title:"js",
    author:"mahbub",
    year:2025,
    price:500
};

for (data in book){
    console.log(data+ "=" + book[data]);
}

//problem 7 nested objects
let person  = {
    name:"Fahim",
    age:16,
    address:{
        city:"Rajshahi",
        country:"Bangaldesh"
    },
    skills : ["infinity"]
}

console.log(person["name"]);
console.log(person.address.country);
console.log(person["skills"]);
