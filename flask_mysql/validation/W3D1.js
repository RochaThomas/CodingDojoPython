
/* 
Given an array of ints representing a line of people where the space between
indexes is 1 foot, with 0 meaning no one is there and 1 meaning someone is in
that space,
return whether or not there is at least 6 feet separating every person.
Bonus: O(n) linear time (avoid nested loops that cause re-visited indexes).
*/

/*
create a function
create a boolean result variable set to true
loop through
if array at index is 1 then set a variable count to 0
for every next iteration that array at index isn't equal to 1 increase by 1
when index is 1 check the count if count is less than 6 then result equals false and break loop
*/

const queue1 = [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1];
// const expected1 = false;

const queue2 = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1];
// const expected2 = true;

/**
 * Determines whether each occupied space in the line of people is separated by
 * 6 empty spaces.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<0|1>} queue
 * @returns {Boolean}
 */
function socialDistancingEnforcer(queue) {
    var result = true;
    var count = 6;
    for (var i = 0; i < queue.length; i++){
        if (queue[i] == 1){
            if(count < 6){
                result = false;
                break;
            }
            else {
                count = 0;
            }
        }
        else {
            count += 1;
        }
    }
    return result;
}

console.log(socialDistancingEnforcer(queue1));
console.log(socialDistancingEnforcer(queue2));

// module.exports = { socialDistancingEnforcer };




// -------------------------------------------------------------------------------------------------------------------------------------------------------------------



/* 
  Balance Index
  Here, a balance point is ON an index, not between indices.
  Return the balance index where sums are equal on either side
  (exclude its own value).
  
  Return -1 if none exist.
  
*/

/*
create a function
create a result variable = -1
if statement that checks to see if the length of array is longer than 2 initially
if not then return result immediately
for loop to go through
nested for loop to carry the index
if sum left = sum right break and return index
*/

const nums1 = [-2, 5, 7, 0, 3];
// const expected1 = 2;

const nums2 = [9, 3, 9];
// const expected2 = 1;

const nums3 = [1, 2, 99, 3]
// const expected3 = 2

const nums4 = [9, 9];
// const expected4 = -1;

// /**
//  * Finds the balance index in the given array where the sum to the left of the
//  *    index is equal to the sum to the right of the index.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {Array<number>} nums
//  * @returns {number} The balance index or -1 if there is none.
//  */
function balanceIndex(nums) {
    var result = -1;
    if (nums.length == 2){
        return result;
    }

    var sumLeft = 0;
    var sumRight = 0;
    for (var i = 0; i < nums.length; i++){
        sumLeft += nums[i];
        sumRight = 0;
        for (var j = i+2; j < nums.length; j++){
            sumRight += nums[j];
        }
        if (sumLeft == sumRight){
            result = i+1
            break;
        }
    }
    return result;
}

console.log(balanceIndex(nums1));
console.log(balanceIndex(nums2));
console.log(balanceIndex(nums3));
console.log(balanceIndex(nums4));

// module.exports = { balanceIndex };
