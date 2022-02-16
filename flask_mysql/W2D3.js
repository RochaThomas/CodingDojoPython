/* 
Parens Valid
Given an str that has parenthesis in it
return whether the parenthesis are valid
*/

const str1 = "Y(3(p)p(3)r)s";
const expected1 = true;

const str2 = "N(0(p)3";
const expected2 = false;
// Explanation: not every parenthesis is closed.

const str3 = "N(0)t ) 0(k";
const expected3 = false;
// Explanation: because the second ")" is premature: there is nothing open for it to close.

const str4 = "a(b))(c";
const expected4 = false;
// Explanation: same number of opens and closes but the 2nd closing closes nothing.

/**
 * Determines whether the parenthesis in the given string are valid.
 * Each opening parenthesis must have exactly one closing parenthesis.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the parenthesis are valid.
 */

/*
create a function

create a countOpen variable 
create a countClosed variable
iterate through counting the open and closed parenthesis
if they open and closed are equal then keep going if not then return false

create a copy of string so we dont destroy the original
iterate through the string until you hit a closing parenthesis
then iterate backwards until you hit a opening parenthesis
if you dont hit one then return false
if you do hit one then create a substring and delete that substring from the copy string
search for another closing parenthesis
 */
function parensValid(str) {
    var countOpen = 0;
    var countClosed = 0;
    var result = true;

    for (var i = 0; i < str.length; i++){
        if (str[i] == '('){
            countOpen++;
        }
        else if (str[i] == ('(')){
            countClosed++;
        }
    }
    if (countOpen != countClosed){
        result = false;
    }

    var clone = str;
    var partOfString = "";
    for (var j = 0; j < clone.length; j++){
        if (clone[j] == ')'){
        }
    }
}

console.log(parensValid(str1))
module.exports = { parensValid };



// ------------------------------------------------------------------------------------------------



/* 
Braces Valid
Given a string sequence of parentheses, braces and brackets, determine whether it is valid. 
*/

const str1 = "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!";
const expected1 = true;

const str2 = "D(i{a}l[ t]o)n{e";
const expected2 = false;

const str3 = "A(1)s[O (n]0{t) 0}k";
const expected3 = false;

/**
 * Determines whether the string's braces, brackets, and parenthesis are valid
 * based on the order and amount of opening and closing pairs.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the given strings braces are valid.
 */
function bracesValid(str) {}

module.exports = { bracesValid };