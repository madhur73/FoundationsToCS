//class dog
var Dog = {
    "name" :"Brownie",
    "legs" : 4,
    "tails": 2

}
//create an object
var testDog = Dog
var testDog2 = Dog
// ways to access their properties.
console.log(testDog.legs)
console.log(testDog["legs"]);

//add new property
testDog.bark = "boew-bow";
console.log(testDog2.bark)