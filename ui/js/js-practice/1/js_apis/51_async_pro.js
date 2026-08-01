//error handing (try and catch)
//normal promise
function checkage(num){
    return new Promise((resolve, reject) =>{
        if(num >= 18){
            console.log("checking age...")
            resolve("You are adult");
        }
        else{
            reject("You are a babby");
        }
    });
    
}

checkage(16)
    .then(result => console.log(result))
    .catch(error => console.error(error));

