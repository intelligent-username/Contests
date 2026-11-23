// https://leetcode.com/problems/the-kth-factor-of-n/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency
// COMPLETE

class Solution {
public:
    int kthFactor(int n, int k) {
        // Initialize the count of factors to 0
        int count = 0;
        
        // Iterate through the factors of n
        for (int i = 1; i <= n; i++) {
            // If i is a factor of n
            if (n % i == 0) {
                // Increment the count of factors
                count++;
                
                // If the count is equal to k, return i
                if (count == k) {
                    return i;
                }
            }
        }
        
        // If there are less than k factors, return -1
        return -1;
    }
};
