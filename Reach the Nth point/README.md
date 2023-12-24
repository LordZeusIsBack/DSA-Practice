<h2><a href="https://www.geeksforgeeks.org/problems/reach-the-nth-point5433/1">Reach the Nth point</a></h2><h3>Medium</h3><hr><div><p>There are <strong>N</strong> points on the road, you can step ahead by 1 or 2 . If you start from a point 0, and can only move from point i to point i+1 after taking a step of length one, find the number of ways you can reach at point <strong>N</strong>. </p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> N = 5
<strong>Output:</strong> 5
<strong>Explanation:</strong> Three ways to reach at 4th
point. They are {1, 1, 1, 1}, {1, 1, 2},
{1, 2, 1} {2, 1, 1}, {2, 2}.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> N = 5
<strong>Output:</strong> 8
<strong>Explanation:</strong> Three ways to reach at 5th
point. They are {1, 1, 1, 1, 1},
{1, 1, 1, 2}, {1, 1, 2, 1}, {1, 2, 1, 1},
{2, 1, 1, 1}{1, 2, 2}, {2, 1, 2}, {2, 2, 1}</pre>
<p>&nbsp;</p>

<p><strong>Your Task:</strong></p>

<p>You don't need to read or print anyhting. Your task is to complete the function <strong>nthPoint()</strong> which takes <strong>N</strong> as input parameter and returns the total number of ways <strong>modulo 10^9 + 7</strong> to reach at <strong>Nth</strong> point.</p>
<p><strong>Expected Time Complexity:</strong> O(N)
<strong>Expected Auxiliary Space:</strong> O(N)

Constraints:
1 <= N <= 10^5</p>
</div>
