class Solution:    
    def countX(self,L,R,X):
        count = 0
        for i in range(L + 1, R):
            if str(X) not in str(i):
                continue
            count += str(i).count(str(X))
        return count

# https://www.geeksforgeeks.org/problems/how-many-xs4514/1