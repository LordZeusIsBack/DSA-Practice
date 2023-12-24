class Solution:
    def nthPoint(self, n):
        a = b = 1

        mod = 10**9 + 7

        for i in range(1, n):
            c = (a + b) % mod
            a, b = b, c

        return b



import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.nthPoint(n)
		print(ans)
