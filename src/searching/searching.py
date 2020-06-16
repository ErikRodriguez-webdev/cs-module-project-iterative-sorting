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
    pass
    # Lowest is always 0
    # Highest is always len(list) - 1
    # Middle is Lowest + Highest / 2

    # trigger = True
    # lowest = 0
    # highest = len(arr) - 1

    # While loop true:
    # if target > middle, then set lowest to middle + 1
    # if target < middle, then set highest to middle - 1
    # while trigger:
    #     middle = (lowest + highest) // 2
    #     print(middle)

    #     if target == middle:
    #         trigger = False
    #         return middle

    #     if target > middle:
    #         lowest = middle + 1

    #     if target < middle:
    #         highest = middle - 1

    return -1  # not found
