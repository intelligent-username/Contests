# WORD HUNT: IN PROGRESS
# https://cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2023/ccc/juniorEF.pdf #5

def main():
    # String of Uppercase letters (TARGET WORD)
    W = input()

    # Number of rows in the grid
    R = int(input())

    # Number of columns in the grid
    C = int(input())
    grid = []

    # Number of times the word appears
    H = 0

    for _ in range(R):
        grid.append(input().split())

    for r in range(R):
        H += check_horizontals(grid[r], C, W)

    print(H)

def check_horizontals(grid_row, columns, word):
    word_found = False
    word_len = len(word)

    for temp in range(columns - word_len + 1):
        # Check if the current letter matches the first letter of the word
        if grid_row[temp] == word[0]:
            frontier = "".join(grid_row[temp:temp + word_len])
            # Check if the frontier matches the word
            if frontier == word:
                word_found = True

    return word_found

def check_verticals():
    ...

def check_diagonals():
    ...

if __name__ == "__main__":
    main()
