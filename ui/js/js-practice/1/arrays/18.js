//array method practice 1
//1 push and pop problem
let fruits = [];
fruits.push("apple", "banana","mango");
fruits.pop();
console.log(fruits);

//2 unshif and shif problem
let nums = [10,20,30]
nums.unshift(5);
nums.shift();
console.log(nums);

//3 map problem
numbers = [1,2,3,4,5];
let double = numbers.map(num => num*2);
let sqr = numbers.map(num => num*num);
console.log(double,sqr);

//4 filter problem
let ages = [12,18,20,25,30,15]
let adults = ages.filter(age => age >= 18);
let oddnumbers = ages.filter(odd => odd % 2 !==0);
console.log(adults,oddnumbers);

//5 reduce problem
let marks = [80, 75, 90, 85, 70]
let total = marks.reduce((n1, n2) => n1 + n2,0);
let average = total / marks.length;
console.log(marks,total,average);

//6 mixed challenge
let words = ["banana", "apple", "mango", "kiwi", "grape"]
let filtered_words = words.filter(word => word.length >= 5);
let uppercase_words = filtered_words.map(word => word.toUpperCase());
console.log(uppercase_words);