from typing import List

class Solution:
    def buyMaximumProducts(self, n: int, k: int, price: List[int]) -> int:
        stocks = [(price[i], i + 1) for i in range(n)]
        stocks.sort()
        total_stocks = 0
        for stock_price, day in stocks:
            stocks_to_buy = min(day, k // stock_price)
            total_stocks += stocks_to_buy
            k -= stocks_to_buy * stock_price

        return total_stocks


        



class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,k = map(int,input().strip().split())
        
        price=IntArray().Input(n)
        
        obj = Solution()
        res = obj.buyMaximumProducts(n, k, price)
        
        print(res)
