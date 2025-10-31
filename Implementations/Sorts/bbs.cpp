// Bubble Sort
// Simplest sort ever

#include <iostream>
#include <vector>

using namespace std;

template<typename T>

void BubbleSort(vector<T>& lst) {
    int len = lst.size();

    while (len > 0) {
        for (int i = 0; i < len - 1; i++) {
            if (lst[i] > lst[i+1]) {
                swap(lst[i], lst[i+1]);
            }
        }
        len--;
    }
}

