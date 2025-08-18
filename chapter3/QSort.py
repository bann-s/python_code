#leetstyle

from typing import List

class my_solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quick_sort(arr, low, high):
            if low < high:
                PIndex = partition(arr, low, high)
                quick_sort(arr, low, PIndex - 1)
                quick_sort(arr, PIndex + 1, high)
        
        def partition(arr, low, high):
            pivot = arr[high]
            i = low - 1
            for j in range(low, high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1

        quick_sort(nums, 0, len(nums) - 1)
        return nums
    

if __name__ == "__main__":
    nums = [3, 6, 8, 10, 1, 2, 1]
    solution = my_solution()
    print("Original array:", nums)  
    sorted_nums = solution.sortArray(nums)
    print("Sorted array:", sorted_nums)