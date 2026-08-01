//async / await
//shortcut to handle promisses

//async function always return promise
//await will stop function until it meets resolve

//exmaple code
async function fetchdata(){
    let data = {
        name:"Fahim",
        age:16
    }
     // no conversion needed
    let result = JSON.stringify(data); // convert object to JSON string
    console.log(result);
}

//calling function
fetchdata();


