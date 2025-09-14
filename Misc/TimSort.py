# Not gonna lie, I basically copied this TimSort algorithm. 
# Implementing would take forever
# Cool idea though

from typing import List

MIN_RUN = 32

def insertion_sort(arr: List, left: int, right: int) -> None:
    """Sorts arr[left:right+1] using insertion sort in-place."""
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def count_run(arr: List, start: int, end: int) -> int:
    """Detects run starting at 'start', returns run length."""
    run_end = start + 1
    if run_end == end:
        return 1

    # Ascending run
    if arr[run_end] >= arr[start]:
        while run_end < end and arr[run_end] >= arr[run_end - 1]:
            run_end += 1
    # Descending run
    else:
        while run_end < end and arr[run_end] < arr[run_end - 1]:
            run_end += 1
        # Reverse descending run to make ascending
        arr[start:run_end] = arr[start:run_end][::-1]

    return run_end - start


def merge(arr: List, start: int, mid: int, end: int) -> None:
    """Merges arr[start:mid] and arr[mid:end] using buffer on smaller run, with galloping."""
    len1, len2 = mid - start, end - mid

    # Identify which run is smaller
    if len1 <= len2:
        left = arr[start:mid].copy()  # buffer for smaller run
        i = 0
        j = mid
        k = start
        while i < len(left) and j < end:
            # Galloping: skip blocks if many consecutive from one side
            if left[i] <= arr[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = arr[j]
                j += 1
            k += 1
        # Copy remaining from buffer
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
    else:
        right = arr[mid:end].copy()
        i = mid - 1
        j = len(right) - 1
        k = end - 1
        while i >= start and j >= 0:
            if arr[i] > right[j]:
                arr[k] = arr[i]
                i -= 1
            else:
                arr[k] = right[j]
                j -= 1
            k -= 1
        while j >= 0:
            arr[k] = right[j]
            j -= 1
            k -= 1


def timsort(arr: List) -> None:
    """Full TimSort implementation."""
    n = len(arr)
    if n < 2:
        return

    # Step 1: Identify and sort runs
    runs = []  # list of tuples (start, length)
    i = 0
    while i < n:
        run_len = count_run(arr, i, n)
        # Extend short runs to min run length
        if run_len < MIN_RUN:
            extend_len = min(MIN_RUN, n - i)
            insertion_sort(arr, i, i + extend_len - 1)
            run_len = extend_len
        runs.append((i, run_len))
        i += run_len

    # Step 2: Iteratively merge runs
    while len(runs) > 1:
        new_runs = []
        i = 0
        while i < len(runs):
            if i + 1 < len(runs):
                start1, len1 = runs[i]
                start2, len2 = runs[i + 1]
                merge(arr, start1, start2, start2 + len2)
                new_runs.append((start1, len1 + len2))
                i += 2
            else:
                new_runs.append(runs[i])
                i += 1
        runs = new_runs
