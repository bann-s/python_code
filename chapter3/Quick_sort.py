#to implement quick sort algorithm 

# This code implements the quick sort algorithm, which is a highly efficient sorting algorithm.
# It works by selecting a 'pivot' element from the array and partitioning the other elements

def quick_sort(arr, low, high):
    if len(arr) == 1:  # If the array has only one element, it is already sorted
        return arr
    if low< high:
        PIndex = partition(arr, low, high )
        #partitioning the array
        quick_sort(arr, low, PIndex - 1)  # Recursively sort elements
        quick_sort(arr, PIndex + 1, high)
        # around the pivot  
    return arr

# around the pivot. The process is repeated recursively for the sub-arrays.

# The partition function is used to rearrange the elements in the array.
def partition(arr, low, high):
    pivot = arr[high]  # Choosing the last element as pivot
    i = low - 1  # Pointer for the smaller element
    for j in range(low, high):
        if arr[j] <= pivot:  # If current element is smaller than or equal to pivot
            i += 1  # Increment index of smaller element
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap the pivot element with the element at i + 1
    return i + 1  # Return the partitioning index


if __name__ == "__main__":
    sample_array = [3, 6, 8, 10, 1, 2, 1]
    sorted_array = quick_sort(sample_array, 0 , len(sample_array) - 1)
    print("Sorted array:", sorted_array)    
# Output: Sorted array: [1, 1, 2, 3, 6, 8, 10]  


"""
i=-1
j=0
arr[j]<=pivot
    i+=1
    arr[i], arr[j] = arr[j], arr[i]  # Swap elements
    j+=1

arr[j]> pivot
    No swap
    j+=1

arr[i], pivot = pivot, arr[i]  # Swap the pivot element with the element at i + 1
    return i + 1  # Return the partitioning index

Time Complexity
Average case: O(n log n)
Worst case: O(n²) (if the pivot is always the smallest/largest element)
Space Complexity
O(log n) (average, due to recursion stack)
O(n) (worst case, if recursion is highly unbalanced)
"""