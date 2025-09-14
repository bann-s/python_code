from typing import List


class Solution:
    def merge_sort(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])
        return self.merge(left, right)

    def merge(self, left: List[int], right: List[int]) -> List[int]:
        result = []
        left_index, right_index = 0, 0
        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1
        result.extend(left[left_index:])
        result.extend(right[right_index:])
        return result


if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    solution = Solution()
    print("Original:", arr)
    print("Sorted:", solution.sortArray(arr))

"""     General slicing syntax: arr[start:stop:step]
        start → index where slicing begins (default = 0).
        stop → index where slicing ends (default = len(array))
        step → how many elements to skip (default = 1)
        
        When you write array[:], it means:
            start = beginning of array
            stop = end of array
            step = 1
            
        arr[1:] → from index 1 to end → [2, 3, 4, 5]
        arr[:3] → from start to index 2 → [1, 2, 3]
        arr[::2] → every 2nd element → [1, 3, 5]
        arr[::-1] → reversed array → [5, 4, 3, 2, 1]
        
        arr = [1, 3, 5, 7, 9, 8, 2, 4, 6, 8, 10]
        
        INDEX   0   1   2   3   4   5   6   7   8   9   10
        ELEMENT 1   3   5   7   9   8   2   4   6   8   10
        
        resultant = arr[: : 3] => arr[::3] picks every 3rd element starting from the beginning
        Start at index 0 → 1
        Next index 3 → 7
        Next index 6 → 2
        Next index 9 → 8
        
        resultant: [1,7,2,8]

        """