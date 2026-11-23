// https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

// Complete
// Little edge cases took way too long. But that means I'm learning

#include <string>

using namespace std;

class Solution {
public:
    int maxVowels(string s, int k) {
        string vowels = "aeiou";
        
        int len = s.size();

        int p1 = 0;
        int p2 = k;

        int max;
        bool found;

        int cntr = 0;

        for (int i = p1; i < p2; i++) {
            found = vowels.find(s[i]) != string::npos; 
            if (found) {
                cntr++;
            }
        }

        max = cntr;

        // Bruh time limit exceeded.
        // Ok let's go back to using the add last, subtract final method
        for (int i = p2; i < len; i++) {

            if (vowels.find(s[i]) != string::npos) {
                cntr++;
            }

            if (vowels.find(s[i - k]) != string::npos) {
                cntr--;
            }

            if (cntr > max) {
                max = cntr;
            }

        }

        return max;
        
    }
};
