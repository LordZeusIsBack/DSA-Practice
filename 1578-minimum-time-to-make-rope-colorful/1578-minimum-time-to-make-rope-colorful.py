class Solution:
  def minCost(self, colors: str, neededTime: List[int]) -> int:
    ans, maxNeededTime = 0, neededTime[0]
    for i in range(1, len(colors)):
        if colors[i] == colors[i - 1]:
            ans, maxNeededTime = ans + min(maxNeededTime, neededTime[i]), max(maxNeededTime, neededTime[i])
        else: maxNeededTime = neededTime[i]
    return ans