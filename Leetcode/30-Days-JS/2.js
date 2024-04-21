// https://leetcode.com/problems/counter/submissions/1238601299/?envType=study-plan-v2&envId=30-days-of-javascript
// Create something I don't remember
// COMPLETE

/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    return function() {
        return n++;
    };
};
