// https://leetcode.com/problems/valid-parentheses
// Easy stack problem

// Complete

#include <stack>
using namespace std;
#include <string>

class Solution {
public:
    bool isValid(string s) {
        
        stack<char> st;
        
        for (char c: s) {
            if (c == '{' || c == '(' || c == '[') {
                st.push(c);
            }
            // if family tree
            else if (!st.empty()) {
                if (st.top() == '{' && c == '}') {
                    st.pop();
                }
                else if (st.top() == '(' && c == ')'){
                    st.pop();
                }
                else if (st.top() == '[' && c == ']'){
                    st.pop();
                }
                else {
                    return false;
                }
            }
            else {
                return false;
            }
        }
        if (st.empty()){
            return true;
        }
        return false;
    }
};
