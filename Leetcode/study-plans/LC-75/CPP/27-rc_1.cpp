// https://leetcode.com/problems/number-of-recent-calls

// Count number of recent calls

    // Easy implementation
    // O(n)
        // Any way to do it faster? 
        // LC-75 specifies this under the 'queue' category, so probably by using a queue
        // We can just have a queue that purges entries older than t-3000
        // Which'll take ~O(1)
        // And this is fine since that's the only purpose of this class.
        // Ok bet

// Complete

#include <vector>

using namespace std;

class RecentCounter {
private:
    vector<int> calls;


public:
    RecentCounter() {
    }
    
    int ping(int t) {
        this->calls.push_back(t);
        int i = calls.size() - 1;

        int begin = t - 3000;

        int tmp = 0;
        while (i > -1 && calls[i] >= begin) {
            tmp++;
            i--;
        }

        return tmp;
    }
};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter* obj = new RecentCounter();
 * int param_1 = obj->ping(t);
 */
