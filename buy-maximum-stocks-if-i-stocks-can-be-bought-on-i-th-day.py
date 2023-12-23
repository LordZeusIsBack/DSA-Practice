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

# https://www.geeksforgeeks.org/problems/buy-maximum-stocks-if-i-stocks-can-be-bought-on-i-th-day/1