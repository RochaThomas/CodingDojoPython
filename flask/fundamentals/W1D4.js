// const str1 = "a x a";
// const expected1 = true;

// const str2 = "racecar";
// const expected2 = true;

// const str3 = "Dud";
// const expected3 = false;

// const str4 = "oho!";
// const expected4 = false;

/**
 * Determines if the given str is a palindrome (same forwards and backwards).
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the given str is a palindrome or not.
 */
function isPalindrome(str) {
    var result = true
    for (var i = 0; i < str.length/2; i++) {
        if (str[i] != str[str.length - 1 - i]){
            result = false;
            break;
        }
    }
    return result;
}

// console.log(isPalindrome(str1))
// console.log(isPalindrome(str2))
// console.log(isPalindrome(str3))
// console.log(isPalindrome(str4))

// const { isPalindrome } = require("./isPalindrome");
const str1 = "what up, daddy-o?";
const expected1 = "dad";

const str2 = "uh, not much";
const expected2 = "u";

const str3 = "Yikes! my favorite racecar erupted!";
const expected3 = "e racecar e";

const str4 = "a1001x20002y5677765z";
const expected4 = "5677765";

const str5 = "a1001x20002y567765z";
const expected5 = "567765";

/*
create a function longestPalindromeSubstring
some result variable containing the longest palindrome
for loop
some logic that identifies repeated characters from opposite ends of the string
create a substring
run substring through isPalindrome() function
if true return substring
*/

// dont use string length and iterate from the back
//iterate from the front of the string 
//it will still take multiple substrings even if the character is repeated


function longestPalindromicSubstring(str) {
    var longest = str[0];
    var sub = "";
    for (var i = 0; i < str.length; i++){
        for (var j = i+1; j < str.length; j++){
            if (str[i] == str[j]){
                sub = str.substring(i,j+1)
                if (isPalindrome(sub) && sub.length > longest.length){
                    longest = sub;
                }
            }
        }
    }
    return longest;
}
console.log(longestPalindromicSubstring(str1));
console.log(longestPalindromicSubstring(str2));
console.log(longestPalindromicSubstring(str3));
console.log(longestPalindromicSubstring(str4));
console.log(longestPalindromicSubstring(str5));