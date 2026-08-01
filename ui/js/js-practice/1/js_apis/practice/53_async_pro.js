/* 
একটা wait(ms) function বানাও
 যেটা নির্দিষ্ট সময় পরে resolve করবে → 
 async/await দিয়ে ব্যবহার করো।
*/

//solution
function wait(ms, data) {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve(data);
        }, ms);
    });
}

async function usewait(){
    try{
    //step 1
       let step1 = await wait(1000, "step1")
       console.log(step1);
    //step 2
        let step2 = await wait(2000, "step2")
        console.log(step2);
    //step 3
        let step3 = await wait(3000, "step3")
        console.log(step3);
    }

    catch(error){
       console.log(error);
    }
}

usewait();