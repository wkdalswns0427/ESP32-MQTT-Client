
var url = 'http://localhost:8000/command'

function esp1(){
    
}

function getTest(url){
    fetch('http://localhost:8000').then((response)=>console.log(response));

}

function esp1(){
    fetch(url,
        {
            method : "POST",
            headers : {
                "Content-Type" : "application/json",
            },
            body: JSON.stringify({
              name: "esp",
              number: 1,
              content: "avalon",  
            }),
        }).then((response)=>console.log(response));
}

function esp2(){
    fetch(url,
        {
            method : "POST",
            headers : {
                "Content-Type" : "application/json",
            },
            body: JSON.stringify({
              name: "esp",
              number: 2,
              content: "avalon",  
            }),
        }).then((response)=>console.log(response));
}

function esp3(){
    fetch(url,
        {
            method : "POST",
            headers : {
                "Content-Type" : "application/json",
            },
            body: JSON.stringify({
              name: "esp",
              number: 3,
              content: "avalon",  
            }),
        }).then((response)=>console.log(response));
}


var check1 = $("input[id='esp1']");
check1.click(function(){
	$("p1").toggle();
});
var check2 = $("input[id='esp2']");
check2.click(function(){
	$("p2").toggle();
});
var check3 = $("input[id='esp3']");
check3.click(function(){
	$("p3").toggle();
});