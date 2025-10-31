// If you have a sorted array

#include <iostream>
#include <vector>

using namespace std;

template<typename T>

/**
 * If the needle is in the haystack,
 * return the position of the needle
 * 
 * Otherwise, return -1
 * 
 * Array must be sorted in ascending order
 * 
 */

bool BinarySearch(const vector<T>& haystack, const T& needle) {
    int lo = 0;
    int h = haystack.size();

    while (lo < h) {
        int m = (lo + h) / 2;
        auto val = haystack[m];
        if (val == needle) {
            return m;
        }
        else if (val < needle) {
            lo = m + 1;
        }
        else {
            h = m;
        }
    }
    return -1;
}

