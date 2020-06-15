def linear_search(arr, target):
    # Your code here
    # Loop with integer for i
    # If list[i] is target then return the index
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Write an iterative implementation of Binary Search


def binary_search(arr, target):
    # Lowest is always 0
    # Highest is always len(list) - 1
    # Middle is Lowest + Highest / 2
    lowest = 0
    highest = len(arr)-1
    middle = (lowest + highest) // 2

    # While loop true:
    # if target is > middle:
    # go to the right
    # else go to the left
    # repeat the process
    while target != middle:
        if target > middle:
            lowest = middle + 1

        if target < middle:
            highest = middle - 1

        if target == middle:
            ind = arr.index(target)
            print(f"{ind} this is the index being returned")
            return ind

        if target != middle:
            break

    return -1  # not found
