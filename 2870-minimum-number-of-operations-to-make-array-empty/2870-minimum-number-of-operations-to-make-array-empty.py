class Solution:
    def minOperations(self, nums: List[int]) -> int:
        mp, count = {}, 0
        for num in nums: mp[num] = mp.get(num, 0) + 1
        for value in mp.values():
            t = value
            if t == 1: return -1
            count += t // 3
            if t % 3: count += 1
        return count