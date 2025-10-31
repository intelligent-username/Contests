# My own implementation of merge sort
# Numbers only for now at least

from __future__ import annotations

def merge_sort(arr: list) -> list:
    """
    Returns a sorted version of the input list.
    Uses merge sort.
    Preconditions:
    - arr is a list of numbers
    """
    sorted_arr = []

    # If the array is already of length 1, merge it
    if len(arr) == 1 or len(arr) == 0:
        return arr
    else:
        halfway = len(arr) // 2
        first = merge_sort(arr[0:halfway])
        second = merge_sort(arr[halfway:])
        sorted_arr = _merge(first, second)
    return sorted_arr

def _merge(arr1: list, arr2: list) -> list:
    """
    Preconditions:
    - arr1 and arr2 are lists
    - arr1 and arr2 are already sorted in ascending order
    """
    
    new_list = []
    while arr1 and arr2:
        if arr1[0] > arr2[0]:
            new_list.append(arr2.pop(0))
        else:
            new_list.append(arr1.pop(0))

    new_list.extend(arr1)
    new_list.extend(arr2)
    return new_list
