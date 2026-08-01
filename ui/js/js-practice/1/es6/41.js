//sol 1
/* setTimeout(() => {

    console.log("Hellow World! ")

}, 3000); */

//sol2

/* function great(name){
    console.log(`Hellow ${name}`);
}

setTimeout(great,2000,"Fahim"); */

//sol 3
/* let messages = [
    "First Message",
    "Second Message",
    "Third Message"
]

function showMessage(msg){
    console.log(msg);
}

setTimeout(showMessage , 1000 , messages[0]);
setTimeout(showMessage , 3000 , messages[1]);
setTimeout(showMessage , 5000 , messages[2]); */

//sol 4
/* let count = 1;

let counter = setInterval(() => {
    console.log(count);
    if (count === 5) {
        clearInterval(counter);
    }
    count++;
}, 1000); */

//sol 5
/* setInterval(() => {
    let now = new Date();
    let time = now.toLocaleTimeString();
    console.log(time);
},1000); */

/* let running = setInterval(() => {
  console.log("Running...");
}, 1000);

setTimeout(() => {
  clearInterval(running);
  console.log("Stopped!");
}, 7000); // stop after 7s */

/* let dots = 1;
let loading = setInterval(() => {
  console.log("Loading" + ".".repeat(dots));
  dots++;
  if (dots > 3) dots = 1; // reset after 3 dots
}, 1000);

setTimeout(() => {
  clearInterval(loading);
  console.log("Done!");
}, 5000); */

let reminder = setInterval(() => {
  console.log("Take a break!");
}, 5000); // every 30s

setTimeout(() => {
  clearInterval(reminder);
  console.log("Reminders stopped.");
}, 120000); // stop after 2 minutes

