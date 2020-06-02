//Global variable
var name = "Madhur";

//local scope
let ourName = "madhur"

//const can never change
const pi = 3.1234442323

//semi-colon is not required, just practise
var b = 2;

console.log(b,name, ourName)

//Initialize the values of variables as values are default to undefined
var a =5

// variable name and functions are cse sensitive.
var CASESENSITIVE = 0;

// increment operatoir 
a++;

// all operators siilt to Java
// a += 1

// \ is escape keyword
var abc = "Hello My Name is \"Madhur \" ";
console.log(abc)
// to avoid this use single quotes
var newAbc = 'Hello "Madhur Here"'
console.log(newAbc)

// Concat strings using + operator
console.log(abc + newAbc)

// find length of string
console.log(abc.length)

//String are immutable

var myString = "Hello World";
// Cant do this myString[0] = 'h'


// boolean 
var flag = false;

// ==== strict equality does not convert types 7 == '7' true
// 7 === '7' false

//switch case break similar to java
// default used same

// type casting string to int
 var s ="54";
 var i = parseInt(s);
 console.log(typeof(i));
