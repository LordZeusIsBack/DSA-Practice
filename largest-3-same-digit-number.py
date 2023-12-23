class Solution:
    def largestGoodInteger(self, num: str) -> str:
        lst = [num[i: i + 3] for i in range(len(num) - 2) if num[i] == num[i + 1] and num[i] == num[i + 2]]
        if lst: return max(lst)
        return ''

# https://leetcode.com/problems/largest-3-same-digit-number-in-string/description