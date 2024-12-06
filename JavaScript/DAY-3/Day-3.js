// lets take a array
var arr=[1,2,3,"sagar",true,["mani","rahul","revanth"],{name:"sai", age:22}]

// Write a code snippet to find the length of an array.
console.log(arr.length) // output: 7

// How do you add an element to the end of an array?
arr.push(undefined)
console.log(arr) // output: [1,2,3,'sagar',true,['mani','rahul','revanth'],{ name: 'sai', age: 22 },undefined ]

// How do you remove the last element from an array?
arr.pop()
console.log(arr) // output: [1,2,3,'sagar',true,['mani','rahul','revanth'],{ name: 'sai', age: 22 }]

// How do you add an element to the beginning of an array?
arr.unshift("vamsi")
console.log(arr) // output: ["vamsi" 1,2,3,'sagar',true,['mani','rahul','revanth'],{ name: 'sai', age: 22 }]

// How can you remove the first element from an array?
arr.shift()
console.log(arr); // OUTPUT:- [2,3,'sagar',true,[ 'mani', 'rahul', 'revanth' ],{ name: 'sai', age: 22 }]
  
// How do you reverse the elements in an array?
arr.reverse();
console.log(arr); // OUTPUT: [{ name: 'sai', age: 22 },[ 'mani', 'rahul', 'revanth' ],true,'sagar',3,2,1]
  
// How can you find the index of a specific value in an array?
console.log(arr.indexOf("sagar")) // OUTPUT: 3

// How can you check if a certain value exists in an array?
console.log(arr.includes('sagar')); // OUTPUT: true

// How can you sort the elements of an array in ascending order?
console.log(arr.sort()) // OUTPUT: [1,2,3,{ name: 'sai', age: 22 },[ 'mani', 'rahul', 'revanth' ],'sagar',true]

// How can you convert an array to a string using commas as separators?
console.log(arr.join(",")) //OUTPUT: 1,2,3,sagar,true,mani,rahul,revanth,[object Object]

// Write a code snippet that adds an element to the end of an array, then removes the first element.
arr=[1,5,9,"sagar","mani"]
arr.push("rahul", "revi")
arr.shift()
console.log(arr); //OUTPUT: [ 5, 9, 'sagar', 'mani', 'rahul', 'revi' ]

// How can you reverse an array and then join the elements into a string?
a=["s","a","g","a","r"]
console.log(a.reverse().join("")); // OUTPUT: ragas

// Write a code that first sorts an array in ascending order, then removes the last element.
var b=[5,33,87,"Mintu","chintu",true,undefined]
b.sort()
b.pop()
console.log(b); // OUTPUT: [ 33, 5, 87, 'Mintu', 'chintu', true ]

// How do you add two elements at the beginning of an array, then remove the first element and find the length of the array?
var b=[5,33,87,"Mintu","chintu",true,undefined]
b.unshift("sagar","rahul")
b.shift()
console.log(b.length); // OUTPUT: 8

// How do you combine two arrays, sort the combined array, and then remove the last element?
arr1=[1,2,3,"sagar","rahul"]
arr2=["mani","revi"]
arr = arr1.concat(arr2)
arr.sort()
arr.pop()
console.log(arr); // OUTPUT: [ 1, 2, 3, 'mani', 'rahul', 'revi' ]

// Question 1: Manage a Guest List
var arr =  ["Alice", "Bob", "Charlie", "David"]
arr.unshift("maxi")
arr.pop()
arr.includes("Bob")
console.log(arr); // OUTPUT: [ 'maxi', 'Alice', 'Bob', 'Charlie' ]

// Question 2: Generate a Sentence
var str ="Learn,Practice,Improve"
console.log(str.split("").reverse( ).join("")); // OUTPUT: evorpmI,ecitcarP,nraeL

// Question 3: Create a Playlist
var a=["Song1", "Song2", "Song3"] 
var b=["Song4", "Song5"]
a=a.concat(b)
a.shift()
a.push("song6")
console.log(a); // OUTPUT: [ 'Song2', 'Song3', 'Song4', 'Song5', 'song6' ]

// Question 5: Extract Favorite Movies
var movies= ["Inception", "Titanic", "Avatar", "Interstellar", "Gladiator"]
movies=movies.slice(1,4).concat(["The Matrix", "The Godfather"]).reverse()
console.log(movies); // OUTPUT: [ 'The Godfather', 'The Matrix', 'Interstellar', 'Avatar', 'Titanic' ]

// Question 7: String Operations on Names
var str=("John,Doe,Jane,Smith")
str=str.split(",")
str1=str.includes("Jane")
console.log(str1); // OUTPUT: true
var str2=str.reverse().join(" ")
console.log(str2); //OUTPUT: Smith Jane Doe John

// Question 8: Length-Based Manipulation
var arr=[1, 2, 3, 4, 5]
arr.shift();
arr.push(6,7);
arr.length;
console.log(arr); // OUTPUT: [ 2, 3, 4, 5, 6, 7 ]

// Question 9: Shopping Cart Operations
var arr=["Milk", "Bread", "Eggs", "Butter"]
arr.includes("Eggs");
arr.pop()
arr.push("Cheese","Juice")
console.log(arr); // OUTPUT: ['Milk', 'Bread', 'Eggs', 'Cheese','Juice']

// Question 10: Rearrange and Combine Names
var a = ["Alice", "Bob", "Charlie"]
var b = ["David", "Eve"]
a = a.reverse().concat(b)
a.unshift("Frank")
console.log(a); // OUTPUT: ['Frank', 'Charlie', 'Bob', 'Alice', 'David', 'Eve']

// Question 11: Shopping Cart Operations
var arr=["Milk", "Bread", "Eggs", "Butter"]
var a = arr.indexOf("Eggs")
arr [a]="Cheese"
arr.unshift("Juice")
console.log(arr);// OUTPUT: ['Juice', 'Milk', 'Bread', 'Cheese', 'Butter']