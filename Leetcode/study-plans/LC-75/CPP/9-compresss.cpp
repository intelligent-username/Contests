// https://leetcode.com/problems/string-compression
// Ok question

#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    int compress(vector<char>& chars) {
        char cur = '\0';
        int cntr = 0;
        int pntr = 0; // position to write next
       
        for (char c : chars) {
            // If samecharacter as what we're already storing
            if (c == cur) {
                cntr++;
            
            // Else what we're storing doesn't match
            } else {
                // Check if not storing anything AT ALL yet.
                if (cur != '\0') {
                    chars[pntr++] = cur;
                    if (cntr > 1) {
                        string cntStr = to_string(cntr);
                        for (char digit : cntStr) {
                            chars[pntr++] = digit;
                        }
                    }
                }
                cur = c;
                cntr = 1;
            }
        }

        // Handle last run
        chars[pntr++] = cur;
        if (cntr > 1) {
            string cntStr = to_string(cntr);
            for (char digit : cntStr) {
                chars[pntr++] = digit;
            }
        }

        return pntr;
    }
};


