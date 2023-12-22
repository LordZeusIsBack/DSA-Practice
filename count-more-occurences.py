from collections import Counter

class Solution:
    def countOccurence(self, arr, n, k):
        min_count, freq_dict, count = n // k, Counter(arr), 0
        for i in freq_dict.values():
            if i > min_count:
                count += 1
        return count

# https://www.geeksforgeeks.org/problems/count-element-occurences/1