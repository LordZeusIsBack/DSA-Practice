class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        result = 0
        for char in s:
            if not char.isdigit():
                break
            result = result * 10 + int(char)
        result *= sign
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        result = max(min(result, INT_MAX), INT_MIN)
        return result

# https://leetcode.com/problems/string-to-integer-atoi/