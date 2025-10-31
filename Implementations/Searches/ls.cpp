// Starting from the basics :)
// Linear Search
// No sorting assumptions

#include <iostream>
#include <vector>

using namespace std;

template<typename T>

bool LS(auto needle, vector<T> Haystack) {
    for (const auto& i : Haystack) {
        if (i == needle) return true;
    }
    return false;
}
