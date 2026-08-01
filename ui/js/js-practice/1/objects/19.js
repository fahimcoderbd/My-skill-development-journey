//js objects
//key -string,name of a property , value:details of that can be anything

//example my object
let fahim = {
    "name":"Fahim",
     age:16,
     "city":"Rajshahi"
};

console.log(fahim); //show my info
console.log(fahim["name"]) //Fahim
console.log(fahim.age) //16

//adding data
fahim.birth = 2008; //2008
fahim.skills = "coding,singing,speech,logical thinking,drwaing etc"; //add these
console.log(fahim);

//update data
fahim["city"] = "Dhaka" //city:Dhaka
console.log(fahim);

//deleting key
let my_langs = {
    "1":"python",
    "2":"js"
}

delete my_langs["1"] //delete "1":"python"
console.log(my_langs)

//functions inside objects method
let js = {
    name:"js",
    message:hello = ()=>{
        console.log("Hellow i am js");
    }
};

js.message()

//loop through objects
let python = {
    name:"python",
    invented:1990,
    desc:"simple,cool,wow"
}

//loop 
 for (data in python){
      console.log(data + "=" +python[data])
 }