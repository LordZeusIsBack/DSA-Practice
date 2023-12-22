class Solution:
    def maximumSumSubarray(self, K, Arr, N):
        current_sum = max_sum = sum(Arr[:K])

        for i in range(K, N):
            current_sum = current_sum + Arr[i] - Arr[i - K]
            max_sum = max(max_sum, current_sum)

        return max_sum

# https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1