
var url_on = 'http://localhost:8000/dummyon'
var url_off = 'http://localhost:8000/dummyoff'

function esp1(){
    var dsc = document.getElementById("discount1");
    if(document.getElementById("esp1").checked == true){
        var carno = document.getElementById("carno1").value;
        console.log("on");
        fetch(url_on,
            {
                method : "POST",
                headers : {
                    "Content-Type" : "application/json",
                },
                body: JSON.stringify({
                name: "esp",
                number: 1,
                content: "avalon", 
                carnumber: carno, 
                }),
            })
            .then(type => type.json())
            .then(json => {
                console.log(json);
                if(json["discount"]==true){
                    console.log("discount!!")
                    dsc.style.display = 'block'
                }
            });
    } else{
        console.log("off");
        fetch(url_off,
            {
                method : "POST",
                headers : {
                    "Content-Type" : "application/json",
                },
                body: JSON.stringify({
                name: "esp",
                number: 1,
                content: "babilon",  
                }),
            }).then((response)=>console.log(response))
            .then(dsc.style.display = 'none');
    }
}

function esp2(){
    var dsc = document.getElementById("discount2");
    if(document.getElementById("esp2").checked == true){
        console.log("on");
        var carno = document.getElementById("carno2").value;
        fetch(url_on,
            {
                method : "POST",
                headers : {
                    "Content-Type" : "application/json",
                },
                body: JSON.stringify({
                name: "esp",
                number: 2,
                content: "avalon",
                carnumber: carno,
                }),
            })
            .then(type => type.json())
            .then(json => {
                console.log(json);
                if(json["discount"]==true){
                    console.log("discount!!")
                    dsc.style.display = 'block'
                }
            });
    }else {
        console.log("off");
        fetch(url_off,
            {
                method : "POST",
                headers : {
                    "Content-Type" : "application/json",
                },
                body: JSON.stringify({
                name: "esp",
                number: 2,
                content: "babilon",  
                }),
            }).then((response)=>console.log(response))
            .then(dsc.style.display = 'none');
    }
}

function esp3(){
    var dsc = document.getElementById("discount3");
    if(document.getElementById("esp3").checked == true){
    var carno = document.getElementById("carno3").value;
    console.log("on");
    fetch(url_on,
        {
            method : "POST",
            headers : {
                "Content-Type" : "application/json",
            },
            body: JSON.stringify({
              name: "esp",
              number: 3,
              content: "avalon",  
              carnumber: carno,
            }),
        })
        .then(type => type.json())
        .then(json => {
            console.log(json);
            if(json["discount"]==true){
                console.log("discount!!")
                dsc.style.display = 'block'
            }
        });
        // .then((response)=>console.log(response.json()))
    } else {
        console.log("off");
        fetch(url_off,
            {
                method : "POST",
                headers : {
                    "Content-Type" : "application/json",
                },
                body: JSON.stringify({
                name: "esp",
                number: 3,
                content: "babilon",  
                }),
            })
            .then((response)=>console.log(response))
            .then(dsc.style.display = 'none');
    }
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