class Solution:
    def isHappy(self, n: int) -> bool:
        seen, cur = [], str(n)
        while cur not in seen:
            num_sum = 0
            seen.append(cur)
            for number in cur:
                num_sum += int(number) ** 2
            if num_sum == 1: return True
            cur = str(num_sum)