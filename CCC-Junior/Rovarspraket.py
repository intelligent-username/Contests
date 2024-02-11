# RovarSpraket: IN PROGRESS
# https://cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2015/stage%201/juniorEn.pdf #3

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
vowels = ["a", "e", "i", "o", "u"]
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t","v", "w", "x", "y", "z"]


# Replace each consonant with:
# 1) The consonant itself
# 2) The vowel closest to the consonent (if a consonent is equidistant from two vowels, pick the one that comes first in the alphabet)
# 3) The next consonant in the alphabet; except z is z

# Vowels stay the same

uncoded = input()
coded = ""

for x in uncoded:
    coded += x

    if x in vowels:
        continue
    else:
        letter_pos = letters.index(x)
        next_vowel_pos = False
        previous_vowel_pos = False
        for r in range(letter_pos, -1, 1):
            if letters[r] in vowels:
                next_vowel_pos = r
        for s in range(letter_pos, 0, -1):
            if letters[s] in vowels:
                previous_vowel_pos = s
        
        if next_vowel_pos < previous_vowel_pos:
            coded += letters[next_vowel_pos]
        else:
            coded += letters[previous_vowel_pos]
        
        if x == "z":
            coded += "z"
        else:
            coded += consonants[consonants.index(x)+1]

print(coded)