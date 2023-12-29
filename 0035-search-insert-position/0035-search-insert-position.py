from bisect import bisect
class Solution:
    def BinarySearch(self, Arr, key):
        low, high = 0, len(Arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if Arr[mid] == key: return mid
            elif Arr[mid] < key: low = mid + 1
            else: high = mid - 1
        return -1
    def searchInsert(self, nums: List[int], target: int) -> int:
        if self.BinarySearch(nums, target) == -1:
            index = bisect(nums, target)
            if index > len(nums):return len(nums)
            return index
        return self.BinarySearch(nums, target)
