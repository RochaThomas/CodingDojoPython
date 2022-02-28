// morning algos

/*
Array: Mode
  
Create a function that, given an array of ints,
returns the int that occurs most frequently in the array.
What if there are multiple items that occur the same number of time?
  - return all of them (in an array)
  - what if all items occur the same number of times?
    - return empty array
*/

/*
create a function
create a key value pair object
iterate through the array counting all the instances of the numbers and add them to the object
keys are the number and count is the value
iterate through the dictionary values recording the highest count
iterate through again and push the keys to an array that have the same count as the highest count
if array length at the end is the same as the beginnning then return an empty array
return the array
*/

const nums1 = [];
// const expected1 = [];

const nums2 = [1];
// const expected2 = [1];

const nums3 = [5, 1, 4];
// const expected3 = [];

const nums4 = [5, 1, 4, 1];
// const expected4 = [1];

const nums5 = [5, 1, 4, 1, 5];
// const expected5 = [5, 1];
//  - order doesn't matter

/**
* Finds the mode or all modes if there are more than one. The mode is the
*    value which occurs the most times in the given array.
* - Time: O(?).
* - Space: O(?).
* @param {Array<number>} nums Test
* @returns {Array<number>} Mode or modes in any order.
*/
function mode(nums) {
    if (nums.length == 1) {
        return nums;
    }
    var dict = {};
    var newArray = []
    for (var i = 0; i < nums.length; i++) {
        if (nums[i] in dict) {
            dict[nums[i]] += 1;
        }
        else {
            dict[nums[i]] = 1;
        }
    }
    var highest_count = 1;
    var num_keys = 0;
    for (key in dict) {
        num_keys += 1;
        if (dict[key] > highest_count) {
            highest_count = dict[key];
        }
    }
    for (key in dict) {
        if (dict[key] == highest_count) {
            newArray.push(parseInt(key));
        }
    }
    if (newArray.length == num_keys){
        newArray = [];
    }
    return newArray;
}

console.log(mode(nums1));
console.log(mode(nums2));
console.log(mode(nums3));
console.log(mode(nums4));
console.log(mode(nums5));

module.exports = { mode };

/*****************************************************************************/