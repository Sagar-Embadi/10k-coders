// QUESTION 1
var str1="I Love Coding"
str1=str1.split(" ").reverse()
str1.push('JavaScript')
str1.pop()
console.log(str1.length); // OUTPUT: 3

//Question 2
var arr1 = [10, 20, 30]
var arr2 = [40, 50]
arr1.shift()
arr1.unshift(100)
arr1=arr1.concat(arr2)
console.log(arr1.indexOf(50)) // OUTPUT: -1
console.log(arr1.slice(2));// OUTPUT: [30,40,50]

// Question 3
var arr = [1, 2, 3, 4, 5]
arr.push(10)
arr.reverse()
arr.pop()
arr.reverse()
console.log(arr.indexOf(3));// OUTPUT: 1

// Question 4
var str= "learning is fun"
str= str.split(" ").reverse()
str.push("indeed")
console.log(str.length); // OUTPUT: 4

// Question 5
var arr1 = [5, 10]
var arr2 = [15, 20, 25]
arr1= arr1.concat(arr2)
arr1.push(30)
arr1.shift()
console.log(arr1.includes(15)); // true
console.log(arr1.slice(1)); // [ 15, 20, 25, 30 ]

// Question 6
var arr = ['apple', 'banana', 'mango', 'orange']
arr.push('grape')
arr.pop()
console.log(arr.includes('banana'));//true
console.log(arr.slice(1,3)); // [ 'banana', 'mango' ]

// Question 7
var arr = [3, 6, 9, 12]
arr.unshift(0)
arr.pop()
arr=arr.concat([15,18])
console.log(arr.indexOf(9)); // 3

//Question 8
var string="welcome to the world"
array=string.split(" ").reverse()
array.push('adventure')
console.log(array.includes('to')); // true
console.log(array);// [ 'world', 'the', 'to', 'welcome', 'adventure' ]

//Question 9
var arr1 = [4, 8, 12] 
var arr2 = [16, 20, 24]
arr2.push(28)
arr=arr1.concat(arr2)
arr=arr.slice(2,6)
arr.reverse()
console.log(arr.indexOf(16)); // 2

//Question 10
var arr = ['dog', 'cat', 'fish', 'bird']
arr.unshift('rabbit')
arr.pop()
str=arr.join("-")
console.log(str.includes('cat')); // true
arr=str.split("-")
console.log(arr.slice(1,3)); // [ 'dog', 'cat' ]