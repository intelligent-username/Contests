// https://leetcode.com/problems/unique-number-of-occurrences

// Complete

#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int, int> seen;

        auto nf = seen.end();
        for (int& n: arr) {
            seen[n]++;
        }

        unordered_set<int> counts;

        for (auto& kv: seen) {
            auto num = kv.second;
            if (counts.find(num) != counts.end()) {
                return false;
            }
            counts.insert(num);
        }

        return true;

    }
};


