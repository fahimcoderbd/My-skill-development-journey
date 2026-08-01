//js promise
//infuture kono kaj hobe(resolve) ki hobena(reject) buzte promisse use kora hoy
/*
promise er 3 ta state:
1.pending -akhono cholce
2.fullfiled -kaj ta hoye gese
3.rejected - kaj ta hoy nai(bartho hoyce)
*/

//exmpale code
const mypromise = new Promise((resolve, reject) => {
    let success = true;

if (success) {
    resolve("The promise is done");
}
else{
    reject("The promise is rejected ");
}
});

mypromise.then(result => {
    console.log(result); //The promise is done (resolve)
}).catch(error =>{
    console.log(error); //The promise is rejected (reject)
})