//js objects -part 3
//Object.keys() , Object.values(), Object.entries()

let my_self = {
    name:"Fahim",
    age:25,
    passion:"programming"
}
 
console.log(Object.keys(my_self)); //show all keys
console.log(Object.values(my_self)); //show all values
console.log(Object.entries(my_self)); //show all values and keys

//Object.freeze() and Object.seal()
//these handle changes permissions and logic

let car = {
    name:"bmw",
    year:2025,
};

Object.freeze(car)  //fully locked can't run del or update
car.year = 2030 //can't change
console.log(car.year)
console.log(car)

let phone = {
    brand: "Iphone",
    model: "16 pro max"
};

Object.seal(phone) //can update but not add or delete
phone.brand = "Samsung" ;
delete phone.brand ;//not work

console.log(phone);

//object destructing
//extract data from object
let pc = {
    cpu:"RYEN",
    ram:16,
    os:"windows"
}

let {cpu,ram,os} = pc;
console.log(cpu);
console.log(ram);
console.log(os);

//spread operator
//copy / merge(unite) objects

let obj1 = {a:1, b:2};
let obj2 = {c:3, d:4}

let merge  = {...obj1, ...obj2} //use ... to merge objects
console.log(merge);

//this keyword inside objects
let fahim = {
    branch:"cse",
    grade: "a+",
    info:function(){
        console.log(this.branch+ "is branch" +this.grade + "is grade");
    }
}

fahim.info();

//objects inside arrays
let students = [
  { name: "Fahim", grade: "A+" },
  { name: "Nayeem", grade: "B" },
  { name: "Ayaan", grade: "A" }
];

for (let s of students) {
  console.log(s.name + " has grade " + s.grade);
}
