//morning algos

/* 
  Given a SORTED array of integers, dedupe the array 
  Because array elements are already in order, all duplicate values will be grouped together.
  Ok to use a new array
  Bonus: do it in O(n) time (no nested loops, new array ok)
  Bonus: Do it in-place (no new array)
  Bonus: Do it in-place in O(n) time and no new array
  Bonus: Keep it O(n) time even if it is not sorted
*/

/*
create a function
make an empty output array
iterate through the input array
if the array at index i is the same as the one before then don't output it to the new array
return the  output array
*/

const nums1 = [1, 1, 1, 1];
// const expected1 = [1];

const nums2 = [1, 1, 2, 2, 3, 3];
// const expected2 = [1, 2, 3];

const nums3 = [1, 1, 2, 3, 3, 4];
// const expected3 = [1, 2, 3, 4];

const nums4 = [1, 1];
// const expected4 = [1];

/**
 * De-dupes the given sorted array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {Array<number>} The given array deduped.
 */
// function dedupeSorted(nums) {
//     var dedupe = [nums[0]];
//     for (var i = 1; i < nums.length; i++){
//         if (nums[i] != nums[i-1]){
//             dedupe.push(nums[i]);
//         }
//     }
//     return dedupe;
// }

function dedupeSorted(nums) {
    var i = 1;
    while (i < nums.length) {
        if (nums[i] == nums[i-1]){
            nums.pop(nums[i]);
        }
        i++;
    }
    return nums;
}

console.log(dedupeSorted(nums1));
console.log(dedupeSorted(nums2));
console.log(dedupeSorted(nums3));
console.log(dedupeSorted(nums4));

// module.exports = { dedupeSorted };



//----------------------------------------------------------------------------------------------



/* 
  Given an array of integers
  return the first integer from the array that is not repeated anywhere else
  If there are multiple non-repeated integers in the array,
  the "first" one will be the one with the lowest index.
*/

/*
create a function
create a key value pair object
iterate through and count the number of times a number occurs
then iterate through loop again, checking the count recorded in the key value pair object
if count is 1 break loop and return that number
*/

const nums1 = [3, 5, 4, 3, 4, 6, 5];
// const expected1 = 6;

const nums2 = [3, 5, 5];
// const expected2 = 3;

const nums3 = [3, 3, 5];
// const expected3 = 5;

const nums4 = [5];
// const expected4 = 5;

const nums5 = [];
// const expected5 = null;

const nums6 = [3, 7, 5, 4, 3, 4, 6, 5];
// const expected6 = 7;

/**
 * Finds the first int from the given array that has no duplicates. I.e., the
 *    item at the lowest index that doesn't appear again in the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number|null} The first int value from the given array that has no
 *    dupes or null if there is none.
 */
function firstNonRepeated(nums) {
    var result = null;
    var dict = {};
    for (var i = 0; i < nums.length; i++){
        if (dict.hasOwnProperty(nums[i])){
            dict[nums[i]] += 1;
        }
        else {
            dict[nums[i]] = 1;
        }
    }
    for (var j = 0; j < nums.length; j++){
        if (dict[nums[j]] == 1){
            result = nums[j];
            break;
        }
    }
    return result;
}

console.log(firstNonRepeated(nums1));
console.log(firstNonRepeated(nums2));
console.log(firstNonRepeated(nums3));
console.log(firstNonRepeated(nums4));
console.log(firstNonRepeated(nums5));
console.log(firstNonRepeated(nums6));

module.exports = { firstNonRepeated };