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
        check_horizontals(W, grid, R, C)


    print(H)

def check_horizontals(word, grid, rows, columns, move = False):
    for row in range(rows):
        for column in range(columns):
            if grid[row][column] == word[column]:
                continue
            else:
                break
                

def check_verticals(word, grid, rows, columns):
    ...

def check_diagonals(word, grid, rows, columns):
    ...

if __name__ == "__main__":
    main()