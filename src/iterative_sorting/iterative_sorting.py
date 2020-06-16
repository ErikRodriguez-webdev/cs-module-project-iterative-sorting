# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        current_index = i
        smallest_index = current_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 lines of code )
        # Your code here
        # if arr[current_index] < arr[smallest_index], then redeclare current as new smallest
        for a in range(current_index + 1, len(arr)):
            if arr[a] < arr[current_index]:
                smallest_index = a
        # TO-DO: swap
        # Your code here
        # declare values and swap
        arr[smallest_index], arr[current_index] = arr[current_index], arr[smallest_index]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    # start looping with len(arr) and grab both current and neighbor values to compare
    # condition to compare neighbors and swap
    for i in range(len(arr) - 1):
        current_index = i
        neighbor_index = current_index + 1
        if arr[current_index] > arr[neighbor_index]:
            tempValue = arr[current_index]
            arr[current_index] = arr[neighbor_index]
            arr[neighbor_index] = tempValue

    return arr


'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''


def counting_sort(arr, maximum=None):
    # Your code here
    pass
    return arr
