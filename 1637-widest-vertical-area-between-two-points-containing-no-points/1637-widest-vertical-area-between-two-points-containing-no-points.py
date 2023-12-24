class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        max_width = 0
        for p1, p2 in zip(points, points[1:]):
            max_width = max(max_width, p2[0] - p1[0])
        return max_width
