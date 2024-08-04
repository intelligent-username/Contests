# WORD HUNT: IN PROGRESS (Will never get done)
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
        check_horizontals(grid[r], R, C, W)


    print(H)

def check_horizontals(grid_row, rows, columns, word):
    finds = 0
    over = False
    word_len = len(word)
    temp = 0
    frontier = ""
    frontier_len = 0
    while not over and columns - word_len > 0:
        if frontier_len == 0:
            if grid_row[temp] == word[0]:
                temp += 1
                frontier += word[0]
                frontier_len += 1
        elif grid_row[temp] == word[frontier_len]:
            frontier += word[frontier_len]
            frontier_len += 1
        
        if frontier == word:
            finds += 1

def check_verticals():
    ...

def check_diagonals():
    ...

if __name__ == "__main__":
    main()