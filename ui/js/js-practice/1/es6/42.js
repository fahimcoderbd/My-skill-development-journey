//json - javascript object notation
//json store data and transfer data
//json is a string

//JSON.PARSE() 
//convert json to js object

 const my_info = `{
 "name":"faim",
    "age":16,
    "address":"court,Rajshahi",
    "hobby":["coding","reading","playing"]
    }`

 const convert = JSON.parse(my_info); //it will convert to js object
 console.log(convert); //printing output

 //for getting specific values
 console.log(convert.name);
 console.log(convert.hobby[1]);
 console.log(convert.age);
 console.log(convert.address);