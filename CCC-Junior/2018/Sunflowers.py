# Sunflower; COMPLETE
# https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2018/stage%201/juniorEF.pdf #4

def main():
    # Get number of rows, columns as N
    N = int(input())
    Log = []

    # Add the rotated/unrotated table to 'Log' list
    for x in range(N):
        Log.append(input().split())

    # Use checker & rotator functions to fix the Log
    Log = checker(Log, N)

    # Then print the output properly
    for row in Log:
        print(" ".join(map(str, row)))

def checker(matrix, size):
    for x in range(size - 1):
        for r in range(size - 1):
            if matrix[x][r] > matrix[x][r + 1] or matrix[x][r] > matrix[x + 1][r]:
                # Recursive call to rotator
                return checker(rotator(matrix), size)
    return matrix

def rotator(matrix):
    # Rotate and return and see
    return list(map(list, zip(*matrix[::-1])))

if __name__ == "__main__":
    main()
