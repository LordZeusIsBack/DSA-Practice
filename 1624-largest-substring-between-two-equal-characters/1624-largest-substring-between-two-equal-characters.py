class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        last_index, max_length = {}, -1
        for i, char in enumerate(s):
            if char in last_index: max_length = max(max_length, i - last_index[char] - 1)
            else: last_index[char] = i
        return max_length