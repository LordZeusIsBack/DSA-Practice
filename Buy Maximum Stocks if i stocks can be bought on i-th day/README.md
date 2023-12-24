<h2><a href="https://www.geeksforgeeks.org/problems/buy-maximum-stocks-if-i-stocks-can-be-bought-on-i-th-day/1">2. Buy Maximum Stocks if i stocks can be bought on i-th day</a></h2><h3>Medium</h3><hr><div><p>In a stock market, there is a product with its infinite stocks. The stock prices are given for <strong>N</strong> where <strong>price[i]</strong> denotes the price of the stock on the ith day.
There is a rule that a customer can buy at most i stock on the ith day.</p>

<p>If the customer has an amount of k amount of money initially. The task is to find out the maximum number of stocks a customer can buy.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> price = [10,7,19], k = 45
<strong>Output:</strong> 4
<strong>Explanation:</strong> A customer purchases 1 stock on day 1, 2 stocks on day 2 and 1 stock on day 3 for 10, 7 * 2 = 14 and 19 respectively. Hence, total amount is 10 + 14 + 19 = 43 and number of stocks purchased is 4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> price = [7,10,4], k = 100
<strong>Output:</strong> 6
</pre>
<p>&nbsp;</p>

<p><strong>Your Task:</strong></p>

<p>You don't need to read input or print anything. Your task is to complete the function <strong>buyMaximumProducts()</strong> which takes an array <strong>price</strong> and an integer <strong>k</strong> and returns an integer as output.</p>
<p><strong>Expected Time Complexity:</strong> O(NlogN)
<strong>Expected Auxiliary Space:</strong> O(N)

Constraints:
1 <= N <= 104
1 <= price[i] <= 104
1 <= k <= 104</p>
</div>
