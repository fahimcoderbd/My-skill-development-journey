//promisses practice

/*
👉 একটা promise বানাও যেটা ৩ সেকেন্ড পরে "Hello World" 
return করবে এবং .then() দিয়ে print করবে।
*/

//solution
/* const promise1 = new Promise((resolve) => {
    setTimeout(() => {
        resolve("Hello World"); //if success
    },3000); //3 sec
}).then((message) => {
    console.log(message); //print the message
}); 

*/

/*একটা function checkNumber(num) বানাও:

যদি num even হয় → resolve("Even number")

যদি num odd হয় → reject("Odd number")

Test করো .then() এবং .catch() দিয়ে। */

//solution

/* const checknum = (num) =>{
       if (num % 2 == 0){
          return Promise.resolve("Even number");
       }
       else{
          return Promise.reject("Odd number");
       }
}

// Call the function and handle the promise
checknum(5)
.then((message) => {
    console.log(message); //if even number
})
.catch((error) => {
    console.log(error); //if odd number
});
 */

/*
একটা promise বানাও যেটা 10 return করবে। তারপর:

×2 করবে

+5 করবে

Final result console এ দেখাবে।
*/ 

//solution

/* const promise2 = new Promise((resolve) => {

    return resolve(10);
       
    })

promise2
//chain 1
.then((num2) => {
  return num2 * 2; //multiply by 2
})
//chain 2
.then((num3) => {
    return num3 + 5; //add 5
})
// Final result
.then((result) => {
    console.log(result); // should print 25
}); */

/*
একটা function wait(ms) বানাও যেটা promise return করবে
 এবং নির্দিষ্ট সময় পরে resolve করবে।
*/

//solution

/* const wait = (ms) =>{
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve(); //resolve after ms
        }, ms);
    });
};

wait(2000).then(() => {
    console.log("2 seconds have passed");
}); */


/*
একটা function fetchUser() বানাও 
যেটা ২ সেকেন্ড delay এর পরে একটা object return করবে 
(যেমন: {id: 1, name: "Fahim"})।
.then() দিয়ে user এর নাম দেখাও।
*/

//solution
/* const fetchuser = (obj={}) => {
    return new Promise((resolve) => {
        setTimeout(() => {
           resolve(obj);
        }, 2000);
    });
};

fetchuser({id: 1, name: "Fahim"})
.then((user) =>{
    console.log(user.name); //Fahim
}) */

    /*
    দুইটা promise বানাও:

প্রথমটা ১ সেকেন্ড পরে "First Done"

দ্বিতীয়টা ২ সেকেন্ড পরে "Second Done"
তারপর Promise.all ব্যবহার করে দুইটার result একসাথে দেখাও।
    */

//solution

/* const p1 = new Promise((resolve) =>{
     setTimeout(() => {
          resolve("First Done");
     }, 1000);
})

const p2 = new Promise((resolve) =>{
     setTimeout(() => {
         resolve("Second Done");
     }, 2000);
})

Promise.all([p1, p2]).then((results) => {
    console.log(results); //show all results
}); */


/*
একটা promise বানাও যেটা 
৫০% chance এ resolve("Success")
 আর ৫০% chance এ reject("Failed") করবে।
.catch() দিয়ে error ধরো।
*/

/* const p3 = new Promise((resolve, reject) => {

    let chance = Math.random() //0 - 1

    if (chance < 0.5){
        resolve("Success");
    }
    else{
        reject("Failed");
    }

});

p3.then((result) => {
    console.log("Output: " ,result)
})

.catch((err =>{
    console.log("Error: ", err)
})) */