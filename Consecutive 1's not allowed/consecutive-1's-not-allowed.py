class Solution:

    def countStrings(self, n):
        end_with_zero = 1
        end_with_one = 1
        mod = 10**9 + 7

        for i in range(2, n + 1):
            new_end_with_zero = (end_with_zero + end_with_one) % mod
            new_end_with_one = end_with_zero
            end_with_zero = new_end_with_zero
            end_with_one = new_end_with_one

        return (end_with_zero + end_with_one) % mod