from collections import Counter

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        char_count = Counter("".join(words))
        for count in char_count.values():
            if count % len(words) != 0:
                return False
        
        return True