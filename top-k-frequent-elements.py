from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = Counter(nums)
        most_common_element = freq_dict.most_common(k)
        return [element for element, count in most_common_element]

# https://leetcode.com/problems/top-k-frequent-elements/