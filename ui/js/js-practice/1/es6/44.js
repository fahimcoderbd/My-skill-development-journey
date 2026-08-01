//json practices

const data = `{"name":"Artipe","city":"Dhaka"}`;

//converting to object
const convert =  JSON.parse(data)
console.log(convert['city']) //printing output

//problem2
const obj = {
    fruit: "mango",
    price:50
}

//converting 
const objtojson = JSON.stringify(obj);
console.log(objtojson) //printing output

//problem 3
const profile = '{"name":"Rahim","hobbies":["football","coding","cycling"]}';

const profile2 = JSON.parse(profile);
console.log(profile2.hobbies[1]) //printing output

//problem 4
const my_info  = {
    name:"Fahim",
    age:16,
    fav_langs : ["js","python","html"],
}

const json = JSON.stringify(my_info);
const JSONtoobj = JSON.parse(json)
console.log(JSONtoobj.name) //printing output

//problem 5
const apiResponse = '{"users":[{"id":1,"name":"Fahim"},{"id":2,"name":"Rahim"}]}';
const parser = JSON.parse(apiResponse);
console.log(parser);

for(const user of parser.users){
    console.log(`name: ${user.name}, id: ${user.id}`) //printing output;
}

