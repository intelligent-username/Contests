// https://leetcode.com/problems/counter-ii/?envType=study-plan-v2&envId=30-days-of-javascript
// Counter 2
// OfflineAudioCompletionEvent

/**
 * @param {integer} init
 * @return {Object} Object containing increment, decrement, and reset functions
 */
var createCounter = function(init) {
    let currentValue = init;

    return {
        increment: function() {
            currentValue += 1;
            return currentValue;
        },
        decrement: function() {
            currentValue -= 1;
            return currentValue;
        },
        reset: function() {
            currentValue = init;
            return currentValue;
        }
    };
};

// Example usage:
const counter = createCounter(5);
console.log(counter.increment()); // 6
console.log(counter.reset());     // 5
console.log(counter.decrement()); // 4