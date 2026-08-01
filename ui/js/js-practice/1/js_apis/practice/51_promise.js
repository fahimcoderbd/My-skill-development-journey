//promisses practice 2

/*
একটা promise বানাও 
যেটা ২ সেকেন্ড পরে
 "Task Done" print করবে।
*/

//solution
/* const promise1 = new Promise((resolve) =>{
    setTimeout(() => {
        resolve("Task Done")
    }, 2000);
})

//printing result
promise1.then((res) => console.log(res)); */


/* 
একটা function isPositive(num) বানাও → 
যদি positive হয় resolve করবে, 
না হলে reject করবে।
 */

//solution

/* const isPositive = (num) =>{
    if(num >0){
        return Promise.resolve("This is true.");
    }
    else{
        return Promise.reject("This is false.");
    }
    }

//result
isPositive(5).then((res) => console.log(res)).catch((err) => console.log(err));
isPositive(-1).then((res) => console.log(res)).catch((err) => console.log(err)); */

/* 
একটা promise বানাও যেটা 20 return করবে → তারপর

×3 করবে

−10 করবে

final result দেখাবে।
*/

//Solution

/* const mypromise = new Promise((resolve) =>{
    return resolve(20);
})

// Proper chaining
mypromise
    .then((num) => num * 3)      // 20 * 3 = 60
    .then((num2) => num2 - 10)     // 60 - 10 = 50
    .then((res) => console.log("The final result is: ", res)); // 50 */

    /* 
    wait(ms) function বানাও (আগের মতো) → এবার chain করে দেখাও:

১ সেকেন্ড পরে "Step 1"

২ সেকেন্ড পরে "Step 2"

৩ সেকেন্ড পরে "Step 3"
    */

//sol

/* function wait(ms, data) {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve(data);
        }, ms);
    });
}
wait(1000, "Step 1").then((res) => console.log(res));
wait(2000, "Step 2").then((res) => console.log(res));
wait(3000, "Step 3").then((res) => console.log(res)); */


/* 
fetch("https://jsonplaceholder.typicode.com/users")
 ব্যবহার করে সব user আনো →

.then() দিয়ে শুধু তাদের নামগুলা console এ দেখাও।
*/

/* fetch("https://jsonplaceholder.typicode.com/users")

.then((res) => res.json()) //converted json
.then((users) =>{
    users.forEach(user => {

       //their name
       console.log(user.name);
        
    });
})

.catch((err) =>{
    console.error("Something wrong" ,err);
})
 */

/* 
দুইটা promise বানাও:

প্রথমটা ১ সেকেন্ড পরে "Loading Posts"

দ্বিতীয়টা ৩ সেকেন্ড পরে "Loading Comments"
 Promise.all দিয়ে একসাথে result দেখাও।
*/

/* const p1 = new Promise((resolve) => {
    setTimeout(() => {
        resolve("Loading Posts");
    }, 1000);
});

const p2 = new Promise((resolve) =>{
    setTimeout(() => {
        resolve("Loading comments");
    },3000);
})

Promise.all([p1, p2]).then((results) => {
    console.log(results); // ["Loading Posts", "Loading comments"]
}); //all results */

/* 
একটা promise বানাও যেটা random number (1–10) return করবে।

যদি number > 5 হয় → resolve("Big number")

না হলে → reject("Small number")
*/

/* const p3 = new Promise((resolve, reject) => {
    const number = Math.floor(Math.random() * 10) + 1;
    if (number > 5) {
        resolve("Big number");
    } else {
        reject("Small number");
    }
});
p3.then(res => console.log(res)).catch(err => console.log(err)); */