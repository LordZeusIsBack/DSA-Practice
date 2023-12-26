<h2><a href="https://www.geeksforgeeks.org/problems/subarray-with-0-sum-1587115621/1">Subarray with 0 sum</a></h2><hr><div><p>Given an array of integers. Find if there is a <strong>subarray</strong> (of size at-least one) with <strong>0 sum</strong>. You just need to return true/false depending upon whether there is a subarray present with 0-sum or not. Printing will be taken care by the driver code.</p>
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = 5, arr = {4,2,-3,1,6}
<strong>Output:</strong> Yes
<strong>Explanation:</strong> 2, -3, 1 is the subarray with sum 0.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> n = 5, arr = {4,2,0,1,6}
<strong>Output:</strong> Yes
<strong>Explanation:</strong> 0 is one of the element in the array so there exist a subarray with sum 0.</pre>
<p>&nbsp;</p>
<p><strong>Your Task</strong></p>

<p>You only need to complete the function <strong>subArrayExists()</strong> that takes <strong>array</strong> and <strong>n</strong> as <strong>parameters</strong> and <strong>returns</strong> true or false.</p>
<p><strong>Expected Time Complexity</strong>: O(n)
<strong>Expected Auxiliary Space</strong>: O(n)

<strong>Constraints</strong>:
1 ≤ n ≤ 10^4
-10^5 ≤ a[i] ≤ 10^5

</div>
