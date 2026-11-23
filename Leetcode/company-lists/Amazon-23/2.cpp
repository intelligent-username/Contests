// https://leetcode.com/problems/optimal-partition-of-string/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency
// COMPLETE

class Solution {
public:
    int partitionString(string s) {
        // Initialize the count of substrings to 1
        int count = 1;
        
        // Initialize a set to keep track of the unique characters in the current substring
        unordered_set<char> unique_chars;
        
        // Iterate through the characters in the string
        for (char c : s) {
            // If the current character is already in the set, it means we need to start a new substring
            if (unique_chars.count(c)) {
                // Increment the count of substrings
                count++;
                
                // Clear the set of unique characters
                unique_chars.clear();
            }
            
            // Add the current character to the set of unique characters
            unique_chars.insert(c);
        }
        
        // Return the count of substrings
        return count;
    }
};
