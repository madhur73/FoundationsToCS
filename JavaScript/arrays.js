// Arrays of mixed data type
var ourArray= ["John", "Dov", 25]

//Similar to python list
console.log(ourArray)

ourArray[0] = "Madhur";
console.log(ourArray)
// multiple dimensions []

//push element in list/ array
ourArray.push(["Abc", "&&&"])
console.log(ourArray);

//similarly pop() removes the last element

//shift is pop(0), removeFirst()
ourArray.shift()
console.log(ourArray);

//unshift is appendatFirst like queue

ourArray.unshift("Happy");
console.log(ourArray);