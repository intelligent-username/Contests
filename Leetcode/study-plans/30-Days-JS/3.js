// https://leetcode.com/problems/to-be-or-not-to-be/?envType=study-plan-v2&envId=30-days-of-javascript
// COMPLETE

/**
 * @param {any} val
 * @return {Object}
 */
var expect = function(val) {
    return {
        toBe: function(expected) {
            if (val === expected) {
                return true;  // Directly return true
            } else {
                throw new Error("Not Equal");
            }
        },
        notToBe: function(expected) {
            if (val !== expected) {
                return true;  // Directly return true
            } else {
                throw new Error("Equal");
            }
        }
    };
};
