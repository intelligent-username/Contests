// https://leetcode.com/problems/number-of-recent-calls

// This time using queue

// Complete

#include <queue>

using namespace std;

class RecentCounter {
    private:
        queue<int> recents;

    public:
        RecentCounter() {}

        int ping(int t) {
            recents.push(t);

            int begin = t - 3000;

            while (!recents.empty() && recents.front() < begin) {
                recents.pop();
            }

            return recents.size();

        }
};
