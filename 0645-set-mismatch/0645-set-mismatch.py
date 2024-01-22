from collections import Counter

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        expected_sum, expected_sum_of_squares, actual_sum, actual_sum_of_squares = n * (n + 1) // 2, n * (n + 1) * (2 * n + 1) // 6, sum(nums), sum(x**2 for x in nums)
        diff_sum = expected_sum - actual_sum
        diff_sum_of_squares = expected_sum_of_squares - actual_sum_of_squares
        duplicate = (diff_sum_of_squares // diff_sum + diff_sum) // 2
        missing = duplicate - diff_sum
        return [missing, duplicate]
