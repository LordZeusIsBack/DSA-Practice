class Solution:
    
    def findMaxSum(self, arr, n):
        if n == 0:
            return 0
        elif n == 1:
            return arr[0]
        incl = arr[0]
        excl = 0
        for i in range(1, n):
            new_incl = excl + arr[i]
            new_excl = max(incl, excl)
            incl = new_incl
            excl = new_excl
        return max(incl, excl)