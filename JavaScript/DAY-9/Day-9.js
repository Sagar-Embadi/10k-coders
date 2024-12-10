function name(){
    var a="sagar"
    console.log(a);    
}
name()

var z=100;
function local(){
    console.log(100+z);
}
console.log(z)
local()

function a(){
    function b(){
        function c(){
            console.log(x);
        }
        c()
    }
    b()
}
var x=100;
a()

var b=300;
function d(){
    function e(){
        console.log(200+b)
    }
    e()
}
b=600
d()
console.log(b)