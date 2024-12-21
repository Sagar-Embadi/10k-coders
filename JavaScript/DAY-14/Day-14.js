// Map Examples
// map: Creates a new array by applying a function to each element of the original array.

// Doubling Numbers: Multiply each number in an array by 2.
const numbers = [1, 2, 3, 4];
const doubled = numbers.map((num) => num * 2);
console.log(doubled); // Output: [2, 4, 6, 8]

// Converting to Uppercase: Transform an array of strings to uppercase.
const fruits = ["apple", "banana", "cherry"];
const upperFruits = fruits.map((fruit) => fruit.toUpperCase());
console.log(upperFruits); // Output: ['APPLE', 'BANANA', 'CHERRY']

// Extracting Property Values: Retrieve the 'name' property from an array of objects.
const users = [
  { name: "Alice", age: 25 },
  { name: "Bob", age: 30 },
  { name: "Charlie", age: 35 },
];
const names = users.map((user) => user.name);
console.log(names); // Output: ['Alice', 'Bob', 'Charlie']

// Calculating Squares: Compute the square of each number in an array.
const number1 = [2, 3, 4];
const squares = number1.map((num) => num ** 2);
console.log(squares); // Output: [4, 9, 16]

// Appending Strings: Add a suffix to each string in an array.
const animals = ['cat', 'dog', 'bird'];
const pluralAnimals = animals.map(animal => animal + 's');
console.log(pluralAnimals); // Output: ['cats', 'dogs', 'birds']

// filter Examples:
// filter: Generates a new array containing elements that meet a specified condition.

//Filtering Even Numbers: Select only even numbers from an array.

const number2 = [1, 2, 3, 4, 5];
const evenNumbers = number2.filter(num => num % 2 === 0);
console.log(evenNumbers); // Output: [2, 4]

// Filtering by String Length: Get strings longer than 3 characters.

const words = ['hi', 'hello', 'hey', 'greetings'];
const longWords = words.filter(word => word.length > 3);
console.log(longWords); // Output: ['hello', 'greetings']

//Filtering Objects by Property: Find objects with a specific property value.

const products = [
  { name: 'Laptop', available: true },
  { name: 'Phone', available: false },
  { name: 'Tablet', available: true }
];
const availableProducts = products.filter(product => product.available);
console.log(availableProducts);
// Output: [{ name: 'Laptop', available: true }, { name: 'Tablet', available: true }]

// Filtering Positive Numbers: Extract positive numbers from an array.

const number3 = [-1, 0, 2, -3, 4];
const positiveNumbers = number3.filter(num => num > 0);
console.log(positiveNumbers); // Output: [2, 4]

// Filtering Non-Null Values: Remove null or undefined values from an array.

const mixedArray = [7, null, 'hello', undefined, 42];
const validValues = mixedArray.filter(item => item != null);
console.log(validValues); // Output: [7, 'hello', 42]

// forEach Examples:
// Logging Array Elements: Print each element of an array.

const colors = ['red', 'green', 'blue'];
colors.forEach(color => console.log(color));
// Output:
// red
// green
// blue

//Calculating Sum: Compute the sum of array elements.

const number4 = [10, 20, 30];
let sum = 0;
number4.forEach(num => sum += num);
console.log(sum); // Output: 60

//Modifying Object Properties: Increase the age property of each object by 1.

const people = [
  { name: 'Alice', age: 25 },
  { name: 'Bob', age: 30 }
];
people.forEach(person => person.age += 1);
console.log(people);
// Output:
// [{ name: 'Alice', age: 26 }, { name: 'Bob', age: 31 }]

//Appending to DOM Elements: Add list items to an unordered list in HTML.

const fruits1 = ['apple', 'banana', 'cherry'];
const ul = document.createElement('ul');
fruits1.forEach(fruit => {
  const li = document.createElement('li');
  li.textContent = fruit;
  ul.appendChild(li);
});
document.body.appendChild(ul);

// apple
// banana
// cherry