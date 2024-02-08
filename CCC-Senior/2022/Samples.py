# Good Samples; IN PROGRESS
# https://cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2022/ccc/seniorEF.pdf #3

N, M, K = input().split()

# Makes a piece with exactly N notes
# Positive int is the pitch of the note
# A sample is good if no two notes in the sample have the same pitch

# N: number of notes
# M: highest accepted pitch
# A piece with exactly K good samples is required

# For example, if N = 3, M = 2, K = 5:

# Possible pitches are:
# [1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [1, 2, 2], [2, 1, 2], [2, 2, 1], [2, 2, 2]

