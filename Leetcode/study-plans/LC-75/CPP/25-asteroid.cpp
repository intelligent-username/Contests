// https://leetcode.com/problems/asteroid-collision

// Asteroid Collisions
// Very annoying

// Compelte

#include <vector>
#include <stack>
#include <algorithm>    

using namespace std;

class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        // Ok this is a bit of a puzzle
        // Luckily I know it's under the "stack" section.

        // Let's form a stack
        // Add the positives to it
        // When there's a negative, pop until a bigger or equal one is found
        // This basically ensures the correctness of motion checking autoatically since we're only using one stack
        // And it's also why my first instinct of using a vector<int> is hugely wrong.

        stack<int> yo;

        for (int& asteroid: asteroids) {
            if (asteroid > 0) {
                yo.push(asteroid);
            }
            else {
                bool destroyed = false;

                while (!yo.empty() && yo.top() > 0) {
                    if (yo.top() < -asteroid) {
                        yo.pop();
                        continue;
                    }
                    else if (yo.top() == -asteroid) {
                        yo.pop();
                        destroyed = true;
                        break;
                    }
                    else {
                        destroyed = true;
                        break;
                    }
                }
                if (!destroyed) {
                    yo.push(asteroid);
                }
            }
        }
        vector<int> ans;
        while (!yo.empty()) {
            ans.push_back(yo.top());
            yo.pop();
        }

        reverse(ans.begin(), ans.end());
        return ans;

    }
};
