class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return next(i for i in nums if nums.count(i) == 1)