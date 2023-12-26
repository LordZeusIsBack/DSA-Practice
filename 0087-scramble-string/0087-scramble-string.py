class Solution:
    def isScramble(self, s1, s2):
        if len(s1) != len(s2):
            return False

        memo = {}

        def helper(s1, s2):
            if (s1, s2) in memo:
                return memo[(s1, s2)]

            if len(s1) == 1:
                memo[(s1, s2)] = s1 == s2
                return memo[(s1, s2)]

            chars = [0] * 26
            for char in s1:
                chars[ord(char) - ord('a')] += 1
            for char in s2:
                chars[ord(char) - ord('a')] -= 1
            for val in chars:
                if val != 0:
                    memo[(s1, s2)] = False
                    return False

            for i in range(1, len(s1)):
                if (helper(s1[:i], s2[:i]) and helper(s1[i:], s2[i:])) or \
                        (helper(s1[:i], s2[-i:]) and helper(s1[i:], s2[:len(s2) - i])):
                    memo[(s1, s2)] = True
                    return True

            memo[(s1, s2)] = False
            return False

        return helper(s1, s2)
