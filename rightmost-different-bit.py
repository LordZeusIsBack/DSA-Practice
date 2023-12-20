class Solution:
    
    def posOfRightMostDiffBit(self, m, n):
        xor_result = m ^ n
        
        if xor_result == 0:
            return -1
        
        position = 1
        while xor_result & 1 == 0:
            xor_result >>= 1
            position += 1
        
        return position

# https://www.geeksforgeeks.org/problems/rightmost-different-bit-1587115621/1