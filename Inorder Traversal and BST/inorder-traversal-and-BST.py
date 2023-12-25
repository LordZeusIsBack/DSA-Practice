class Solution:
    def isRepresentingBST(self, arr, N):
        stack = []
        root = float('-inf')
        for i in range(N):
            if arr[i] <= root:
                return 0
            root = arr[i]
        return 1