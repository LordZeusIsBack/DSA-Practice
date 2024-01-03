class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans, v = 0, []
        for a in bank:
            s = a
            cnt = s.count('1')
            if cnt != 0: v.append(cnt)
        for i in range(1, len(v)):
            t = v[i] * v[i - 1]
            ans += t
        return ans