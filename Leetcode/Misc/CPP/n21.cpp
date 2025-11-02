// https://leetcode.com/problems/water-bottles
// Warmup
// C

// Complete

class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        // How many water bottles can youn DRINK
        // So, all the ones you start with
        // Once you dirnk those, you have that many EKPTY ones
        // PLUS the // of how many you have with how many EMPTY ones will trade for a full one
        // Keep adding how many full ones you have
        
        int totalDrunk = numBottles;
        // int empty_bottles = numBottles;  // After drinking all the initial bottles, they become empty

        // (While you have enough empty bottles to exchange for full ones)
        while (numBottles >= numExchange) {
            int newBottles = numBottles / numExchange;
            totalDrunk += newBottles;
            numBottles = newBottles + (numBottles % numExchange); // New full + leftover empty
        }

        return totalDrunk;
    }
};
