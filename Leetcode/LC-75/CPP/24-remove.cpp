// https://leetcode.com/problems/removing-stars-from-a-string

// Removing stars from a string

// Complete

#include <vector>
#include <string>

using namespace std;

class Stac {
private:
    vector<char> data;
public:
    void push(char val) {
        data.push_back(val);
    }

    char pop() {
        if (data.empty()) return '\0';

        char val = data.back();
        data.pop_back();
        return val;
    }

    char peek() {
        return data.empty() ? '\0' : data.back();
    }

    string word() {
        string s(data.begin(), data.end());
        return s;    }

};

class Solution {
public:
    string removeStars(string s) {
        Stac a;
        string result = "";

        for (char c: s) {
            if (c == '*') {
                a.pop();
            }
            else {
                a.push(c);
            }
        }

        return a.word();

    }
};
