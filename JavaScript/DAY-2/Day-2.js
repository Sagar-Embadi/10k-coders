// TERNARY OPERATOR
// true/false? Ture statement : false statement;

var num1=5
var num2=6
num1<=num2 ? console.log(num1,"is less than or equal to",num2): console.log(num1,"is greater than or equal to",num2)
// OUTPUT: 5 is less than or equal to 6

// ASSIGNMENT OPERATORS

var a=5
console.log(a+=5); // 10 a=a+5
console.log(a*=5); // 50 a=a*5
console.log(a/=10); // 5 a=a/10
console.log(a-=2); // 3  a=a-2

// LOGICAL OPERATORS

if (10 && 10){
    console.log("logical && satisfied");
}else{
    console.log("logical && is not satisfied");
}
// OUTPUT: logical && satisfied

if (null || undefined){
    console.log("logical || satisfied");
}else{
    console.log("logical || is not satisfied");
}
// OUTPUT: logical || is not satisfied

console.log(!true) // false (! converts truthy to falsy value and vice versa...)