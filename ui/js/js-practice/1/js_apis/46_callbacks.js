//callbacks
//callback akta function jeta akata onno function ke argument send kore
//etar por onno function ta jokhon call hobe tokhon callback function ta o call hobe

//simple callback
function greeting(name){
    console.log('Hello '+name);
}

function takeinput(callback){
    const name = 'Fahim';
    callback(name);
}
takeinput(greeting);