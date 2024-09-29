class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0: return False
        while str(n)[-1] == '5' or str(n)[-1] == '0': n //= 5
        while sum([int(digit) for digit in str(n)]) % 3 == 0: n //= 3
        while str(n)[-1] in ['2', '4', '6', '8', '0']: n //= 2
        if n == 1: return True
        return False