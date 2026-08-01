//json.stringify()
//convert js to json
//need this wen we want to send data to the server

const fahim = {
    name: 'Fahim',
    age:16,
    gender:"boy"
}

const convert = JSON.stringify(fahim);
console.log(convert);