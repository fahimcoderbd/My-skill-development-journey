//number guessing game

let attemps = 0; //collect attempts
let generated_num = Math.floor(Math.random() * 10) + 1;

const app = () =>{
    const secret = generated_num;
    const guess = Number(prompt("Enter guess: "));
    attemps++;
     
    if(guess == secret){
        alert("You win bro!");
        alert("You attemps are: ", attemps)
    }

    else{
        alert("Na Na bro you lose!")
    }

    //cheking the secret number
    console.log(secret);
}

app();