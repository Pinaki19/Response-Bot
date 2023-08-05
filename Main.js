main();

function main() {
    const form = document.body;
    //console.log(form);
    
    let child = form.children;
    //console.log(child);
    var i;
    for (i = 0; i < child.length; i++) {
        if (child[i].tagName == "DIV") {
            break;
        }
    }

    var not_ques = new Set();
    var filled = new Set();
    var p = child[i].children[1].children[0].children[1].children[0].children[1].children;
    //console.log(p);
    
    var k, x;
    for (k = 0; k < p.length; k++) {
        x = p[k].children[0];
        //console.log(x.children[0]);
    
        try {
            x = x.children[0].children[1];
            //console.log(x.children[1].getAttribute("role"));
            //console.log(x);
            
            if (x.children[1].getAttribute("role") == "list") {
                filled.add(k);
                x = x.children[1];
                var l = x.childElementCount;
    
                if(l==1){
                    x.children[0].childre[0].children[0].click();
                }
                else if (true) {
                    var select = Math.floor(Math.random() * (l - 1))
                    //console.log(select);
                    x.children[select].children[0].children[0].click();
                    select = Math.floor(Math.random() * (l - 1));
                    //console.log(select);
                    x.children[select].children[0].children[0].click();
                    select = Math.floor(Math.random() * (l - 1));
                    //console.log(select);
                    x.children[select].childre[0].children[0].click();
                }
                

            }
            else {
                x = x.children[1].children[0];
                x = x.children[0].children[0].children;
                //console.log(x);
                var select = Math.floor(Math.random() * x.length)
                x[select].children[0].click();
            }

        }
        catch (e) {
            not_ques.add(k);
            //console.log("Not ques"+k+e);
            console.log("not ques"+p[k])
        }


    }
    //alert("sub");
    setTimeout(sub,400);
}

function sub() {
    document.forms[0].submit();
    return;
}
