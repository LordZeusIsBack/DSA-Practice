from math import pow
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        if (dividend > 0 and divisor < 0) or (divisor > 0 and dividend < 0):
            dividend, divisor = abs(dividend), abs(divisor)
            if dividend // divisor > pow(2, 31):
                return -1 * pow(2, 31)
            return -1 * (dividend // divisor)
        if dividend // divisor > pow(2, 31):
            return pow(2, 31)
        return dividend // divisor
