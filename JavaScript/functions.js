// function is the keyword here def funct => function
var myGlobal =10

function wordBlanks(myNoun, myAdj, myVerb, myAdverb){

    var result = myNoun+myAdj+myVerb+myAdverb;

    return result
}
function checkArguments(a,b)
{
    if(typeof myGlobal != "undefined"){
        console.log(myGlobal)
        oopsGlobal =5
    }
    return a+b
}
console.log(wordBlanks("dog","big","ran", "quickly."))
console.log(checkArguments(1,4));

// Scope represent visibility of variables
// no var written  GLOBAL is the scope

// anonymous function, no name
// => instead of writing "function"

const magic = () => new Date();

console.log("New Date Anonymous",magic)

const conArr = (arr1,arr2) => arr1.concat(arr2);
console.log(conArr([1,2,3],[4,5]))