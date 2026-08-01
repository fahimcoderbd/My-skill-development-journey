//innertext
//only show the html text and ignore other html tags

const get_heading = () =>{
    let heading = document.getElementById('heading').innerText;
    console.log(heading); //show only the text
}

get_heading();

//innerhtml 
//show full html tags with the text

const get_html = () =>{
    let text = document.getElementById('heading').innerHTML;
    console.log(text); //show full code
}

get_html();