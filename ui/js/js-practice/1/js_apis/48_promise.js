//kivabe then and catch kaj kore\

//.then() > jokhon resolve ba kaj succes hoy
//.catch() > jokhon kaj fail hoy ba reject hoy

//example fetching mock data from server
//mock data
const data = {
    name:"Fahim",
    age:16
}

/* console.log(data); */

function loadData(){
    return new Promise((resolve,reject)=>{
    
        setTimeout(()=>{
            let getdata = data;
            if(getdata = true){
                resolve("Data Loaded success!")
                console.log(getdata);
            }
            else{
                reject("Data Loaded failed!")
            }
        },2000)
    
    });
}

loadData()
.then(data => console.log(data)) 
.catch(err => console.log(err));