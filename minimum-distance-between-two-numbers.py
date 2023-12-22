class Solution:
    def minDist(self, arr, n, x, y):
        index_x = -1
        index_y = -1
        min_distance = float('inf')

        for i in range(n):
            if arr[i] == x:
                index_x = i
                if index_y != -1:
                    min_distance = min(min_distance, abs(index_x - index_y))
            elif arr[i] == y:
                index_y = i
                if index_x != -1:
                    min_distance = min(min_distance, abs(index_x - index_y))

        if index_x == -1 or index_y == -1:
            return -1

        return min_distance

# https://www.geeksforgeeks.org/problems/minimum-distance-between-two-numbers/1