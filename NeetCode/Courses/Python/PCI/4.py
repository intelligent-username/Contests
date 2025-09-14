# https://neetcode.io/problems/python-sort-lambda

from typing import List


def sort_words(words: List[str]) -> List[str]:
    return sorted(words, key=lambda word: len(word), reverse=True)


def sort_numbers(numbers: List[int]) -> List[int]:
    return sorted(numbers, key=lambda num: abs(num))


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
