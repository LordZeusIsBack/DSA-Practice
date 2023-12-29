class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        lst = list(sorted(set(nums)))
        for i in lst:
            if nums.count(i) > len(nums)/2:
                return i