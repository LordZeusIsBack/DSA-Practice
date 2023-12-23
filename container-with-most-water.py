class Solution:
    def maxArea(self, height: List[int]) -> int:
        f, r, area = 0, len(height) - 1, 0
        while(f < r):
            area = max(area, (r - f) * min(height[f], height[r]))
            if height[f] < height[r]: f += 1
            else: r -= 1
        return area

# https://leetcode.com/problems/container-with-most-water/description/