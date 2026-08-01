//arrays

let numbers = [1,2,3,4,5];
let my_name = ["fahim", "abrar", "niloy"];

//printing values
console.log(numbers);
console.log(my_name);
//accessing items with indexing
console.log(my_name[0]); //fahim

//push() method
//add elements to the end of an array
let nums = [1,2,3,4,5];
nums.push(6); //add 6 to the end
console.log(nums);

//pop() method
//removes from the end
let nums2 = [1,2,3,4,5];
let last = nums2.pop(); //remove 5
console.log(nums2);

//unshift() method
//add from the beginning
let num3 = [1,2,3];
num3.unshift(0); //add 0
console.log(num3)

//shift() method
//remove from the beginning
let num4 = [1,2,3];
num4.shift(1); //remove1
console.log(num4);

//map() method
//it uses a function to chnage the items
let num5 = [1,2,3];
let sqr = num5.map(num => num * num);
console.log(sqr) //[1,4,9]

//filter() method
//to search any items
let num6 = [1,2,3,4];
// odd number ber korobo
let oddnums = num6.filter(num => num % 2 !== 0);
console.log(oddnums); //[1,3]

//reduce method()
//it uses a function to converts to a single value
let num7 = [1,2,3,4,5,6]
//sum all 
let sum = num7.reduce((acc, curr) => acc + curr,0);
console.log(sum) //21

//array methods() finished....