
/*
  Sum To One Digit
  Implement a function sumToOne(num)​ that,
  given a number, sums that number’s digits
  repeatedly until the sum is only one digit. Return
  that final one digit result.
  Tips:
    to access digits from a number, need to convert it .toString() to access each digit via index
    parseInt(arg) returns arg parsed as an integer, or NaN if it couldn't be converted to an int
    isNaN(arg) used to check if something is NaN
*/

const num1 = 5;
const expected1 = 5;

const num2 = 10;
const expected2 = 1;

const num3 = 25;
const expected3 = 7;

const num4 = 59437 // -> 28 --> 10 --> 1

/*
create a function
have a result variable
input name -> string
if string length is 1 then return the number
else use a for loop to iterate through the string parse the character to an int and add it to the result variable
return sumToOneDigit(result)
*/

/**
 * Sums the given number's digits until the number becomes one digit.
 * @param {number} num The number to sum to one digit.
 * @returns {number} One digit.
 */
function sumToOneDigit(num) {
    if (num < 10) {
        return num;
    }
    var result = 0;
    var stringNum = num.toString();
    for (var i = 0; i < stringNum.length; i++) {
        result += parseInt(stringNum[i]);
    }
    return sumToOneDigit(result);
}

console.log(sumToOneDigit(num1));
console.log(sumToOneDigit(num2));
console.log(sumToOneDigit(num3));
console.log(sumToOneDigit(num4));

module.exports = { sumToOneDigit };

/*****************************************************************************/

// http://algorithms.dojo.news/static/Algorithms/index.html#LinkTarget_2129
/* 
  String Anagrams
  Given a string,
  return array where each element is a string representing a different anagram (a different sequence of the letters in that string).
  Ok to use built in methods
*/

const str1 = "lim";
const expected1 = ["ilm", "iml", "lim", "lmi", "mil", "mli"];
// Order of the output array does not matter

/*
create a function
create an anagrams array variable []
if array length is equal to string.length factorial then return array
else switch the letters around and call the function again
*/

/**
 * Add params if needed for recursion.
 * Generates all anagrams of the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {Array<string>} All anagrams of the given str.
 */

function factorial(n) {
    n = Math.floor(n);
    if (n == 1) {
        return 1;
    }
    else if (n == 0) {
        return 1;
    }
    else if (n < 0) {
        return -1;
    }
    else {
        return n * factorial(n-1);
    }
}

function generateAnagrams(str) {
    var anagrams = [];
    if (anagrams.length == factorial(str.length)){
        return anagrams;
    }
    else {
        var firstLetter = str[0];
        var restOfString = str.slice(1);
        for (var i = 0; i < restOfString.length; i++){
            
        }
    }
}

module.exports = { generateAnagrams };

/*****************************************************************************/