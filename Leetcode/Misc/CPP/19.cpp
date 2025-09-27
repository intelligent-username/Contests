// https://leetcode.com/problems/largest-triangle-area/
// Daily Challenge
// Brute force is SUPER easy
// Optimized is 'hard' level difficulty I reckon
// COMPLETED

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    double largestTriangleArea(vector<vector<int>>& points) {
        // Think of all n points
        // They are randomly scattered
        // We can form a perimeter that contains all the points
        // This is done by picking all of the 'outermost' points
        // This perimeter is called the 'Convex Hull'
        // Hull for outer shell, convex indicating there are no inward dents
        // So let's get to it

        // First sort the points
        sort(points.begin(), points.end(),
        [](const vector<int>& a, const vector<int>& b) {
            return a[0] == b[0] ? a[1] < b[1] : a[0] < b[0];
        });

        // Then pass them to the Hull maker
        vector<vector<int>> hull = makeHull(points);

        // Now we may or may not have far fewer points, but likely will.
        
        // Time to actually compute which area is the smallest
        int h = hull.size();
        int max_area = 0;
        for (int i = 0; i < h; i++) {
            int k = (i + 2) % h;
            for (int j = (i + 1) % h; j != i; j = (j + 1) % h) {
                while (true) {
                    int next_k = (k + 1) % h;
                    int area1 = abs(cross_diff(hull[i], hull[j], hull[k]));
                    int area2 = abs(cross_diff(hull[i], hull[j], hull[next_k]));
                    if (area2 > area1) {
                        k = next_k;
                    } else {
                        break;
                    }
                }
                int new_area = abs(cross_diff(hull[i], hull[j], hull[k]));
                if (new_area > max_area) {
                    max_area = new_area;
                }
                if ((j + 1) % h == i) break; // prevent infinite loop
            }
        }
        return max_area / 2.0;
    }

    vector<vector<int>> makeHull(vector<vector<int>>& points) {
        // Assuming the points are sorted in ascending order of x-coordinates, ties broken by y-coordinates
        vector<vector<int>> lower;
        vector<vector<int>> upper;

        size_t len = points.size();

        for (size_t i = 0; i < len; i++) {
            while (lower.size() >= 2) {
                auto &A = lower[lower.size() - 2]; // second last
                auto &B = lower[lower.size() - 1]; // last
                auto &C = points[i];               // current point

                // If their cross product is negative
                if (cross_diff(A, B, C) <= 0) {
                    lower.pop_back(); // remove last point
                } else {
                    break; // we made a left turn
                }
            }
            lower.push_back(points[i]); // add current point
        }

        for (int i = len - 1; i >= 0; i--) { // reversed order for upper hull
            while (upper.size() >= 2) {
                auto &A = upper[upper.size() - 2]; // second last
                auto &B = upper[upper.size() - 1]; // last
                auto &C = points[i];               // current point

                // If their cross product is negative
                if (cross_diff(A, B, C) <= 0) {
                    upper.pop_back(); // remove last point
                } else {
                    break; // we made a left turn
                }
            }
            upper.push_back(points[i]); // add current point
        }

        if (lower.size() > 0) lower.pop_back();        // drop rightmost duplicate
        if (upper.size() > 0) upper.pop_back();        // drop leftmost duplicate

        // append upper in reverse order, skipping upper[0] (leftmost)
        for (int i = (int)upper.size() - 1; i >= 0; --i) {
            lower.push_back(upper[i]);
        }

        return lower;
    }
    
    // int since all points are integers.
    int cross_diff(const vector<int>& point1, const vector<int>& point2, const vector<int>& point3) 
    {
        return (point2[0] - point1[0]) * (point3[1] - point1[1])
            - (point2[1] - point1[1]) * (point3[0] - point1[0]);
    }
};
