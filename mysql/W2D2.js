
/* 
  Given a string,
  return a new string with the duplicates excluded
  Bonus: Keep only the last instance of each character.
*/

/*
create a function
create a variable that will hold the result string
run for loop to iterate through the string (maybe in reverse order to handle bonus case)
if statement to check if the char at index of the string is already in the new string
if not copy it over
if it is then do not copy
return the string at the end
*/

const str1 = "abcABC";
// const expected1 = "abcABC";

const str2 = "helloo";
// const expected2 = "helo";

// bonus test case
const str3 = "abcdeab"
// const expected3 = "cdeab"


/**
 * De-dupes the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string that may contain duplicates.
 * @returns {string} The given string with any duplicate characters removed.
 */
function stringDedupe(str) {
    var result = "";
    for (var i = str.length - 1; i >= 0; i--){
        if (result.includes(str[i]) == false){
            result = str[i] + result;
        }
    }
    return result;
}

console.log(stringDedupe(str1));
console.log();

console.log(stringDedupe(str2));
console.log();

console.log(stringDedupe(str3));
console.log();
// module.exports = { stringDedupe };


// -----------------------------------------------------------------------


/* 
Given a string containing space separated words
Reverse each word in the string.
If you need to, use .split to start, then try to do it without.
*/

/*
/*
create a function
create a result variable that going to be a string
create an array of all the words using .split
use a for loop to iterate through the words in the array
reverse every individual array using .reverse or using a for loop
concatinate the reversed word to the result string
return the final result string
*/

const str1 = "hello";
// const expected1 = "olleh";

const str2 = "hello world";
// const expected2 = "olleh dlrow";

const str3 = "abc def ghi";
// const expected3 = "cba fed ihg";

/**
 * Reverses the letters in each words in the given space separated
 * string of words. Does NOT reverse the order of the words themselves.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str Contains space separated words.
 * @returns {string} The given string with each word's letters reversed.
 */
function reverseWords(str) {
    var result = "";
    var words = str.split(' ');
    console.log(words);

    for (var i = 0; i < words.length; i++){
        for (var j = words[i].length - 1; j >= 0; j--){
            result += words[i].charAt(j);
        }
        if (i != words.length - 1){
            result += " ";
        }
    }
    return result;
}

console.log(reverseWords(str1));
console.log();

console.log(reverseWords(str2));
console.log();  

console.log(reverseWords(str3));
console.log();

// module.exports = { reverseWords };


// -----------------------------------------------------------------------


/* 
Reverse Word Order
Given a string of words (with spaces)
return a new string with words in reverse sequence.
*/

const str1 = "This is a test";
const expected1 = "test a is This";

/**
 * Reverses the order of the words but not the words themselves form the given
 * string of space separated words.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} wordsStr A string containing space separated words.
 * @returns {string} The given string with the word order reversed but the words
 *    themselves are not reversed.
 */
function reverseWordOrder(wordsStr) {}

module.exports = { reverseWordOrder };