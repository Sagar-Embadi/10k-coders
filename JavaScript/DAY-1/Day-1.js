// Code for Voting Eligibility..

var age =prompt("Enter your age: ");
if (age>=18){
    console.log("Your are eligible to vote")
}else{
    console.log("your are not eligible to vote")
}

// OUTPUT for above code :--

    // age=18 ==> returns- Your are eligible to Vote
    // age=17 ==> returns- Your are not eligible to vote

// Code for Marriage Eligibility

var gender=prompt("Enter your gender: ");
var age = prompt("Enter your age: ");
if (gender=='male'){
    if (age>=21){
        console.log("Your are eligible for marriage")
    }else{
        console.log("Your are not eligile for marriage")
    }
}else{
    if (age>=18){
        console.log("Your are eligible for marriage")
    }else{
        console.log("Your are not eligile for marriage")
    }
}
// OUTPUT: --

    // gender = 'male' , age = 21 ==> returns:- Your are eligible for marriage
    // gender = 'male' , age = 17 ==> returns:- Your are not eligible for marriage

    // gender = 'female' , age = 18 ==> returns:- Your are eligible for marriage
    // gender = 'female' , age = 17 ==> returns:- Your are not eligible for marriage

// Code for Driving License Eligibility..

var age = prompt("Enter your age: ");
if (age>=18){
    console.log("person is eligible to apply for a driving license.")
}else{
    console.log("person is not eligible to apply for a driving license.")
}
//OUTPUT:--

    // age = 22 ==> returns:- person is eligible to apply for a driving license.
    // age = 15 ==> returns:- person is not eligible to apply for a driving license.

// Code for Exam Eligibility..

var marks = prompt("Enter your marks: ");
if (marks>=75){
    console.log("student is eligible to appear for an exam")
}else{
    console.log("student is not eligible to appear for an exam")
}
//OUTPUT: ---

    // marks = 74.5 ==> returns:- student is not eligible to appear for an exam
    // marks = 80 ==> returns:- student is eligible to appear for an exam

// Code for Senior Citizen Discount Eligibility

var age = prompt("Enter your age: ");
if (age>=60){
    console.log("person qualifies for a senior citizen discount")
}else{
    console.log("person not qualifies for a senior citizen discount")
}

// OUTPUT: --

    // age= 65 ==> returns:- Person qualifies for a senior citizen discount
    // age= 55 ==> returns:- Person not qualifies for a senior citizen discount