let a=+prompt("enter digit here");
let count=0;

for(i=1;i<=a;i++){
   if(a % i==0){
        count++
   }
}
if(count==2){
    console.log(a , "is prime")
}else{
    console.log(a , "is not prime")
}

// output: 
    // 5 -- 5 is prime
    // 20 -- 20 is not prime