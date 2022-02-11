
/* 
  Zip Arrays into Map
  
  
  Given two arrays, create an associative array (aka hash map, an obj / dictionary) containing keys from the first array, and values from the second.
  Associative arrays are sometimes called maps because a key (string) maps to a value 
 */
// start off with a def function 
// define the object that we're returning 
// for loop that reads through both arrays 
// some logic that adds in the keys and values 
// return object 
  

const keys1 = ["abc", 3, "yo"];
const vals1 = [42, "wassup", true];
const expected1 = {
  abc: 42,
  3: "wassup",
  yo: true,
};

/**
 * Converts the given arrays of keys and values into an object.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string>} keys
 * @param {Array<any>} values
 * @returns {Object} The object with the given keys and values.
 */
function zipArraysIntoMap(keys, values) {
    var result = {};
    for (var i = 0; i < keys.length; i++){
        result[keys[i]] = values[i];
    }
    return result;
}
console.log(zipArraysIntoMap(keys1, vals1));

// module.exports = { zipArraysIntoMap };

/*****************************************************************************/

/* 
Invert Hash
A hash table / hash map is an obj / dictionary
Given an object / dict,
return a new object / dict that has the keys and the values swapped so that the keys become the values and the values become the keys
*/

const obj1 = { name: "Zaphod", charm: "high", morals: "dicey" };
// const expected1 = { Zaphod: "name", high: "charm", dicey: "morals" };

/*
create a function 
create 2 variables for two empty arrays
create result variable
use for loop to iterate through keys and values
push keys to one array and values to another
use zipArraysIntoMap function to create a result object
return new result object
*/

/**
* Inverts the given object's key value pairs so that the original values
* become the keys and the original keys become the values.
* - Time: O(?).
* - Space: O(?).
* @param {Object<string, string>} obj An object with string keys and string values.
* @return The given object with key value pairs inverted.
*/
function invertObj(obj) {
    var result = {};
    var arr1 = [];
    var arr2 = [];
    // for (const [key, value] of Object.entries(obj)) {
    //     arr1.push(key);
    //     arr2.push(value);
    // }
    for (key in obj){
        result[obj[key]] = key;
    }

    // result = zipArraysIntoMap(arr2, arr1);
    return result
}

console.log(invertObj(obj1));

module.exports = { invertObj };

/*****************************************************************************/