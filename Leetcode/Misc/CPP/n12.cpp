// https://leetcode.com/problems/implement-router
// This was a daily challenge
// Very annoying to finish
// Especially the searching

#include <unordered_set>
#include <map>
#include <vector>
#include <deque>
#include <algorithm>
#include <tuple>

using namespace std;

struct tuple_hash {
    size_t operator()(const tuple<int,int,int>& t) const {
        auto h1 = hash<int>()(get<0>(t));
        auto h2 = hash<int>()(get<1>(t));
        auto h3 = hash<int>()(get<2>(t));
        return h1 ^ (h2 << 1) ^ (h3 << 2); // combine hashes
    }
};

class Router {
public:
    int memoryLimit;
    deque<tuple<int, int, int>> storage; 
    unordered_set<tuple<int,int,int>, tuple_hash> packets;
    map<int, vector<int>> destTimeTimestamps; // destination -> sorted timestamps

    Router(int memoryLimit): memoryLimit(memoryLimit) {
        storage.clear();
        packets.clear();
        destTimeTimestamps.clear();
    }
    
    bool addPacket(int source, int destination, int timestamp) {
        tuple<int, int, int> packet = {source, destination, timestamp};

        if (packets.find(packet) != packets.end()) {
            return false;
        }

        if (storage.size() >= memoryLimit) {
            auto rem = storage.front();
            storage.pop_front();
            packets.erase(rem);
            int remDest = get<1>(rem);
            int remTime = get<2>(rem);
            auto& tsVec = destTimeTimestamps[remDest];
            tsVec.erase(lower_bound(tsVec.begin(), tsVec.end(), remTime));
            if (tsVec.empty()) destTimeTimestamps.erase(remDest);
        }

        storage.push_back(packet);
        packets.insert(packet);

        // Insert timestamp in sorted order
        auto& tsVec = destTimeTimestamps[destination];
        tsVec.insert(upper_bound(tsVec.begin(), tsVec.end(), timestamp), timestamp);

        return true;
    }
    
    vector<int> forwardPacket() {
        vector<int> forwarded;
        if (storage.empty()) return forwarded;

        auto packet = storage.front();
        storage.pop_front();
        packets.erase(packet);

        int dest = get<1>(packet);
        int time = get<2>(packet);
        auto& tsVec = destTimeTimestamps[dest];
        tsVec.erase(lower_bound(tsVec.begin(), tsVec.end(), time));
        if (tsVec.empty()) destTimeTimestamps.erase(dest);

        forwarded.push_back(get<0>(packet));
        forwarded.push_back(dest);
        forwarded.push_back(time);
        return forwarded;
    }
    
    int getCount(int destination, int startTime, int endTime) {
        if (destTimeTimestamps.find(destination) == destTimeTimestamps.end()) return 0;
        auto& tsVec = destTimeTimestamps[destination];
        auto lb = lower_bound(tsVec.begin(), tsVec.end(), startTime);
        auto ub = upper_bound(tsVec.begin(), tsVec.end(), endTime);
        return ub - lb;
    }
};

/**
 * Your Router object will be instantiated and called as such:
 * Router* obj = new Router(memoryLimit);
 * bool param_1 = obj->addPacket(source,destination,timestamp);
 * vector<int> param_2 = obj->forwardPacket();
 * int param_3 = obj->getCount(destination,startTime,endTime);
 */
