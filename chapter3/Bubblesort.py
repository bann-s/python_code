
def Bubblesort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr) - i -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap if the element found is greater than the next element
    return arr  # Return the sorted array

if __name__ == "__main__":
    sample_array = [64, 34, 25, 12, 22, 11, 90]
    sorted_array = Bubblesort(sample_array)
    print("Sorted array:", sorted_array) 
    
     # Output: Sorted array: [11, 12, 22, 25, 34, 64, 90]
# This code implements the bubble sort algorithm, which is a simple sorting algorithm that repeatedly steps through
# the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the
# list is repeated until the list is sorted. The algorithm gets its name from the way larger elements "bubble" to the top
# of the list.
# The time complexity of bubble sort is O(n^2) in the worst and average cases
# and O(n) in the best case (when the array is already sorted).
# The space complexity is O(1) since it only requires a constant amount of additional space