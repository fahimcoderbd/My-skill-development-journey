//problem 1
let book = {
  name: "Mater js",
  author: "Fahim Abrar",
  price: 500
}

console.log(Object.keys(book)); //printing object keys
console.log(Object.values(book)); //printing values
console.log(Object.entries(book)); //printing entries

//problem 2
let bike = {
  brand: "Yamaha",
  year: 2022
}

/* Object.freeze(bike); //freezing
bike.brand = "ktm"; //updating 
console.log(bike); //printing the whole object */

Object.seal(bike);
bike.brand = "suzuki";
console.log(bike);

//adding new property to bike
bike.owner = "Fahim abrar"
// console.log(bike);

//problem 3
let student = {
  name: "Nusrat",
  myclass: 9,
  section: "B",
  roll: 15
};

let { name, myclass, roll } = student;
console.log(name);
console.log(myclass);
console.log(roll);

//problem 4
let objA = { x: 10, y: 20 };
let objB = { z: 30, y: 99 };

let unite = { ...objA, ...objB }
console.log(unite);

//problem 5
let person = {
  firstName: "Fahim",
  lastName: "Abrar",
  fullName: function () {
    return this.firstName + " " + this.lastName;
  }
};

let result = person.fullName();
console.log(result);

//problem 6
let players = [
  { name: "Shakib", runs: 75 },
  { name: "Tamim", runs: 50 },
  { name: "Mushfiq", runs: 100 }
];

for (run of players) {
  console.log(run.name + " " + run.runs)
}

const tops = players.filter(p => p.runs > 70);
console.log(tops);