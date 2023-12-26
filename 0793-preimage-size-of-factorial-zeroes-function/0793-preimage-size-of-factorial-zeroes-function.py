from bisect import bisect_left

class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def count_trailing_zeroes(x):
            if x == 0:
                return 0
            return x // 5 + count_trailing_zeroes(x // 5)
        def left_boundary_of_k(k):
            return bisect_left(range(5 * k), k, key=count_trailing_zeroes)
        return left_boundary_of_k(k + 1) - left_boundary_of_k(k)