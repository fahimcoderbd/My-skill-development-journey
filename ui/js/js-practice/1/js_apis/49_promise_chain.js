//promise chaining
//it will return a promise output to the next one

//exmaple chaining 1
//the value is 5
let numpromise = new Promise((resolve, reject) => {

resolve(5); //it will return 5

});

console.log(numpromise);

//chain 2

numpromise.then(num =>{
    console.log(`Number: ${num}`); //5 asbe

    return num * 2 //10
})

//chain 3
.then((num) => {
    console.log(`Number: ${num}`); //10 asbe

    //10+3
    return num + 3; //13 asbe
    })

//chain 4
.then((num) => {
    console.log(`Final Number: ${num}`); //13 asbe
    })
.catch((error) =>{
    console.log("Something went wrong");
})