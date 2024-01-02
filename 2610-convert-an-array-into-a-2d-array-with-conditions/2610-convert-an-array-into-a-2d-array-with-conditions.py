from collections import defaultdict
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        mp, ans = defaultdict(int), []
        for i in nums: mp[i] += 1
        while mp:
            temp = []
            for key, value in list(mp.items()):
                temp.append(key)
                value -= 1
                if value == 0: del mp[key]
                else: mp[key] = value
            ans.append(temp)
        return ans