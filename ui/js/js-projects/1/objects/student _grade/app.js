//grade calculator
//taking grades as input

let grades = [];//store grades here

let subjects = parseInt(prompt("How many subject wanna add: "));

const grade_app = (sub) =>{
    //initializing the grades array
    let storage = grades;

    for (user = 1; user <= sub; user++){
        let subject = prompt(`Enter the subject: ${user}`) //taking subject
        let mark = parseInt(prompt(`Enter marks: ${subject}`)); //taking marks of subject
   
            //pushing data to grades
         storage.push({
            name:subject,
            mark:mark
         });
         };
     }

const calculate_average= (grades) =>{
       for (nums of grades){
          let total = grades.reduce((n1,n2) => n1+n2,0) //getting the total
          console.log(total);
       }
}

grade_app(subjects);