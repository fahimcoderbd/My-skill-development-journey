//age checker app

const age = prompt("Enter your age: "); //taking user age

const checker = (ag) =>{
    if(ag > 18 || age == 18){
        alert("Bro you are adult! ")
    }
    else{
        alert("Na Na bro you are baby!")
    }
}

checker(age);