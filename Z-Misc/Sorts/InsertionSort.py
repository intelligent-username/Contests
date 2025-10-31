# My own implementation of insertion sort
# Numbers only for now. Maybe in the future, implement a more generalized "greater than" comparison that can be called for anything (strings, etc.)

def insertion_sort(lst):
    """
    Uses insertion sort to sort the given list in ascending order.
    In-place.
    """
    length = len(lst)

    for x in range(1, length):
        temp = lst[x]       # Value of current element
        pointer = x - 1     # Pointer to partitioned part

        # Shift larger elements one position to the right
        while pointer >= 0 and lst[pointer] > temp:
            # Kind of like saying, "Take Out" the temporary value and put something in its place
            lst[pointer + 1] = lst[pointer]
            pointer -= 1

        # And once the right spot has been foudn for the tmep,
        # Insert the saved element into the right position
        lst[pointer + 1] = temp       
