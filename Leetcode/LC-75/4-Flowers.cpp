// https://leetcode.com/problems/can-place-flowers/submissions/1236896815/?envType=study-plan-v2&envId=leetcode-75
// COMPLETE

class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int count = 0;
        int m = flowerbed.size();
        int i = 0;
        
        while (i < m) {
            if (flowerbed[i] == 0) {
                int prev = (i == 0) ? 0 : flowerbed[i - 1];
                int next = (i == m - 1) ? 0 : flowerbed[i + 1];
                
                if (prev == 0 && next == 0) {
                    flowerbed[i] = 1;
                    count++;
                }
            }
            
            i++;
        }
        
        return count >= n;
    }
};
