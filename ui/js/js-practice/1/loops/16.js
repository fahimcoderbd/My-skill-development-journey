//loops

//for loop 
//printing numrber from 1 to 10

for (let num = 1; num <= 10;num++){
    console.log(num);
}

//printing my name
for (let fahim = 0; fahim < 5; fahim++){
    console.log("My name is Fahim");
}

//orinting odd numbers in reverse order
for (let i = 5; i >= 1; i--){
    if(i % 2 !== 0)
    //printing odd number
    console.log(i);
}

//while loop
let count = 1

while (count <= 5){
    console.log(count);
    count++;
}

/*
The above while loop prints numbers from 1 to 5.
It increments the count variable after each iteration.
The loop stops when count becomes greater than 5.
*/

let my_age = 16;

do {
    console.log(my_age);
    my_age++
} while (my_age <= 18);

//for off loop 
//used to repeat over arraus,strings and collections
let fruits = ["apple", "banana", "mango"];

for (let fruit  of fruits){
    console.log(fruit)
}

//for in loop
//used for itereting over obkect keys

let person = {
    name: "Fahim",
    age: 16,
    country: "Bangladesh"
};

for (let data in person) {
    console.log(data, ":", person[data]); 
}

//break -stop immediately
//continue -skips the current iteration

for (let i = 1; i <= 5; i++){
    if (i === 3) continue
    if (i === 5) break
    console.log(i)
}