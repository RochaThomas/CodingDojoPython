/* 
    Given an array of strings
    return a sum to represent how many times each array item is found (a frequency table)
    Useful methods:
    Object.hasOwnProperty("keyName")
    - returns true or false if the object has the key or not
    Python: key in dict
*/

const arr1 = ["a", "a", "a"];
// const expected1 = {
//     a: 3,
// };

const arr2 = ["a", "b", "a", "c", "B", "c", "c", "d"];
// const expected2 = {
//     a: 2,
//     b: 1,
//     c: 3,
//     B: 1,
//     d: 1,
// };

const arr3 = [];
// const expected3 = {};

/*
create a function
create a key value pair object variable 
use a for loop to iterate through array
use if statement to check if key is already in key value pair object
if not count the number of times that char is in the array using a nested for loop
at the end of the nest for loop add the char to the result object as a key and the count as the value
*/

/**
 * Builds a frequency table based on the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string>} arr
 * @returns {Object<string, number>} A frequency table where the keys are items
 *    from the given arr and the values are the amnt of times that item occurs.
 */
function frequencyTableBuilder(arr) {
    var result = {};
    for (var i = 0; i < arr.length; i++){
        if (result.hasOwnProperty(arr[i]) == false){
            var count = 1;
            for (var j = i + 1; j < arr.length; j++){
                if (arr[j] == arr[i]){
                    count++;
                }
            }
            result[arr[i]] = count;
        }
    }
    return result;
}

console.log(frequencyTableBuilder(arr1));
console.log();

console.log(frequencyTableBuilder(arr2));
console.log();

console.log(frequencyTableBuilder(arr3));
console.log();

// module.exports = { frequencyTableBuilder };

/*****************************************************************************/


// https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/

/* 
Given a non-empty array of odd length containing ints where every int but one
has a matching pair (another int that is the same)
return the only int that has no matching pair.
*/

/*
multiple solutions...
first thought
create a function
create an object set equal to a function call of frequencytablebuilder that has the arr as the argument
iteratet through the keys in the key value pair object
if statement to see if value % 2 == 0
if != 0 then print out the key and break loop

another solution...?
maybe faster...use same logic as algo before
create a key value pair object
use a for loop to iterate through array
if the value at arr[index] isn't in the key value pair object count how many times it is in the array
if count is odd then break the for loop and return the value

do key value pair objects use more memory than an array? if so then use an array instead of an object
*/

const nums1 = [1];
// const expected1 = 1;

const nums2 = [5, 4, 5];
// const expected2 = 4;

const nums3 = [5, 4, 3, 4, 3, 4, 5];
// const expected3 = 4; // there is a pair of 4s but one 4 has no pair.

const nums4 = [5, 2, 6, 2, 3, 1, 6, 3, 2, 5, 2];
// const expected4 = 1;

// function oddOccurrencesInArray(nums) {
//     var result = null;
//     var freqTable = frequencyTableBuilder(nums);
//     for (key in freqTable){
//         if (freqTable[key] % 2 != 0){
//             result = key;
//             break;
//         }
//     }
//     return result;
// }

function oddOccurrencesInArray(nums) {
    var result = null;
    var freqTable = {}
    for (var i = 0; i < nums.length; i++){
        if (freqTable.hasOwnProperty(nums[i]) == false){
            var count = 1;
            for (var j = i + 1; j < nums.length; j++){
                if (nums[j] == nums[i]){
                    count++;
                }
            }
            if (count % 2 != 0){
                result = nums[i];
                break;
            }
            else {
                freqTable[nums[i]] = count;
            }
        }
    }
    return result;
}

console.log(oddOccurrencesInArray(nums1));
console.log();

console.log(oddOccurrencesInArray(nums2));
console.log();

console.log(oddOccurrencesInArray(nums3));
console.log();

console.log(oddOccurrencesInArray(nums4));
console.log();

/*****************************************************************************/
