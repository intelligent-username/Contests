// https://leetcode.com/problems/top-k-frequent-elements

// Complete

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // Ok I'll try to use a heap
        // A modified heap
        // So the main value (for the max-heap) will be the number of appearances
        // So at the root, we have the node with the biggest appearance value
        // Then, the other value in the node will be the actual number who's appearances we're counting.
        // Once we receive k, just pop k times and apend the numbers

        // I don't think there's any quick/efficient way to store into a heap right away
        // Maybe there is but I'll need to think about it.
        // For now I'll just insert into a regular priority queue and then add that queue to a heap

        
        unordered_map<int, int> counts;

        for (const int n: nums) counts[n]++;

        // Again there's probably a quicker way but I haven't thought about this for long enough
        vector<pair<int, int>> vec;
        for (auto const& [value, count] : counts) {
            vec.push_back({count, value});
        }

        // Make into a heap
        make_heap(vec.begin(), vec.end());

        // Then just pop

        vector<int> ans;

        // I think the > 0 is redundant
        while (k-- > 0) {
            pop_heap(vec.begin(), vec.end());
            ans.push_back(vec.back().second); 
            vec.pop_back();                   
        }

        return ans;

    }
};
