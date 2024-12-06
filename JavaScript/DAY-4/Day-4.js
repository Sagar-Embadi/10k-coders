// STRING METHODS TASKS------

var str1="    sagar"
var str2="embadi    "
str1=str1.trimStart()
str2=str2.trimEnd()
console.log(str1.concat(str2).toUpperCase())
// OUTPUT:- SAGAREMBADI

var str="POOSALAMANIKANTA"
str=str.slice(7,11)
console.log(str.length-1);
console.log(str.toLowerCase());
// OUTPUT:- 3 / mani

var char="E"
var a=char.concat("sagar")
a=a.toUpperCase()
console.log(a.slice(-2,-1))
// OUTPUT:- A

var s1="vamshi"
var s2="Krishna"
s1=s1.slice(0,3)
s2=s2.slice(-3)
var s12= s1.concat(s2)
s12=s12.at(0).toUpperCase()+s12.at(s12.length-1).toUpperCase()
console.log(s12);
// OUTPUT:- Vamhna

var astr= "        revanth      "
astr=astr.trim()
astr=astr.at(0).toUpperCase()+astr.slice(1,astr.length-1)+astr.at(astr.length-1).toUpperCase()
console.log(astr);
// OUTPUT:- RevantH

var hello = "hello there , how are you"
hello=hello.split(" ")
hello=hello.indexOf("are")
console.log(hello);
// OUTPUT:- 4

// OBJECT METHODS TASKS-----

var person = { firstname:"Sagar",lastname:"Embadi", age:22}
console.log(person.firstname); // OUTPUT: Sagar
person.city="New York"
console.log(person);
// OUTPUT: { firstname: 'Sagar', lastname: 'Embadi', age: 22, city: 'New York' }

var product={name:"Iphone",price:"$2500",instock:true}
product.price="$3600"
delete product.instock
console.log(product);
// OUTPUT:-- { name: 'Iphone', price: '$3600' }

var library={fantasy:["Book1","Book2"],mystery:["Book3","Book4"]}
library.scienceFiction=["Book5","Book6"]
console.log(library.fantasy[0]); // OUTPUT: Book1
delete library.mystery
console.log(library);// OUTPUT: { fantasy: [ 'Book1', 'Book2' ], scienceFiction: [ 'Book5', 'Book6' ] }

var user={username:"Sagar",email:"sagarembadi7@gmail,com", address:{city:"HYD",state:"TS",zipcode:500027}}
Object.freeze(user)
user.email="embadisagar2601@gmail.com"
console.log(Object.isFrozen(user)); // OUTPUT: true
user.phone=9493004681
console.log(user);
// OUTPUT: no Change -- {username: 'Sagar',email: 'sagarembadi7@gmail,com',address: { city: 'HYD', state: 'TS', zipcode: 500027 }}

var car={make:"tata" , model:"nexon", price:1500000}
Object.seal(car)
delete car.make
console.log(Object.isSealed(car));//OUTPUT: true
car.price=1300000
console.log(car);//OUTPUT: { make: 'tata', model: 'nexon', price: 1300000 }