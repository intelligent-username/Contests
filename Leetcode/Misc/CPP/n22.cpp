// https://leetcode.com/problems/water-bottles-ii/
// Water Bottles Problem 2
// Done

class Solution {
public:
    int maxBottlesDrunk(int numBottles, int numExchange) {
        int total = numBottles;

        // Basically same as Water Bottles (i) just with an extra step 
        while (numBottles >= numExchange) {
            // Exchange once
            numBottles = numBottles - numExchange + 1; // lose empty, gain 1 full, drink it

            total++;
            numExchange++;
        }

        return total;
    }
};
