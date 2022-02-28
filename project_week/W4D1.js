//morning algos

const string1 = ["h", "e", "l", "l", "o"];
const expected1 = "hello";

const string2 = ["h", "e", "l", "l", "o", " ", "wo", "rld"]
const expected2 = "hello world"

/**
 * Add params if needed for recursion
 * Recursively build a string out of an array of strings.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string>} strings
 * @returns {string} The result of combining all of the strings from the input array.
 */
function buildString(strings) {
    if (strings.length == 0){
        return 0
    }
    else if (strings.length == 1){
        return strings[0]
    }
    return strings[0] + buildString(strings.slice(1));
}

console.log(buildString(string1));
console.log(buildString(string2));

const num1 = 5;
const expected1 = 15;
// Explanation: (1+2+3+4+5)

const num2 = 2.5;
const expected2 = 3;
// Explanation: (1+2)

const num3 = -1;
const expected3 = 0;

/**
 * Recursively sum the given int and every previous positive int.
 * - Time: O(?).
 * - Space: O(?).
 * @param {number} num
 * @returns {number}
 **/
function recursiveSigma(num) {
    if (num <= 0){
        return 0;
    }
    else {
        return Math.floor(num) + Math.floor(recursiveSigma(num - 1));
    }
}

console.log(recursiveSigma(num1));
console.log(recursiveSigma(num2));
console.log(recursiveSigma(num3));