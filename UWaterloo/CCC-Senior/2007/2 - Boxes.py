# COMPLETE
# https://cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2007/stage1/seniorEn.pdf

packaging_volumes = []

def main():
    dimensions = []
    packages = []

    n = int(input("Number of different boxes available: "))

    for i in range(n):
        # Length Width Height in mm
        temp = input(f"Dimensions of box #{i + 1}: ").split(" ")
        dimensions.append([int(x) for x in temp])

    m = int(input("Number of items to be packaged: "))

    for j in range(m):
        temp = input(f"Dimensions of item #{j + 1}: ").split(" ")
        packages.append([int(x) for x in temp])

    # Find and sort the possible packaging values
    for i in dimensions:
        packaging_volumes.append(volume_finder(i))
    packaging_volumes.sort()

    # Find the volume of each item
    item_volumes = []
    for x in packages:
        item_volumes.append(volume_finder(x))

    matches = []

    # Check the volume of each item and assign box to it
    for k in item_volumes:
        matches.append(min_box_finder(k))

    for a in matches:
        if a:
            print(a)
        else:
            print("Item does not fit")


def volume_finder(dimensions):
    volume = dimensions[0] * dimensions[1] * dimensions[2]
    return volume


def min_box_finder(item_volume):
    for d in packaging_volumes:
        if item_volume < d:
            return d
    return False


if __name__ == "__main__":
    main()
