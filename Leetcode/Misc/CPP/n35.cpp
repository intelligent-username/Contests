// https://leetcode.com/problems/find-all-people-with-secret
// Daily problem

// COMPLETE

#include <vector>
#include <algorithm>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <queue>

using namespace std;

class Solution {
public:
    vector<int> findAllPeople(int n, vector<vector<int>>& meetings, int firstPerson) {
        
        set<int> knowers;

        knowers.insert(0);
        knowers.insert(firstPerson);

        // This is the position for time
        int t = 2;
        
        // Sort by time for convenience
        // Maybe sorting isn't necessary but I can't think of any other way
        sort(meetings.begin(), meetings.end(), 
        [t](const vector<int>& a, const vector<int>& b) {
            return a[t] < b[t]; // Just learnt this: must using strict ordering!!
        });

        int i = 0;
        int len = meetings.size();

        while (i < len) {
            int time = meetings[i][t];

            vector<pair<int,int>> curr;

            while (i < len && meetings[i][t] == time) {
                curr.push_back({meetings[i][0], meetings[i][1]});
                i++;
            }

            // Now we've formed our current batch. The biggest problem is 
            // sharing the secret to multiple people simultaneously
            // Then search to find connections
            // And add to knowers

            unordered_map<int, vector<int>> graph;
            for (auto &meeting : curr) {
                int x = meeting.first;
                int y = meeting.second;
                graph[x].push_back(y);
                graph[y].push_back(x);
            }

            queue<int> q;
            unordered_set<int> visited;

            for (auto &[u, _] : graph) {
                if (knowers.count(u)) {
                    q.push(u);
                    visited.insert(u);
                }
            }

            while (!q.empty()) {
                int u = q.front(); q.pop();
                knowers.insert(u);

                for (int v : graph[u]) {
                    if (!visited.count(v)) {
                        visited.insert(v);
                        q.push(v);
                    }
                }
            }

        }

        // Convert knowers to list :)

        vector<int> answer(knowers.begin(), knowers.end());

        // And we're done

        return answer;

    }
};
