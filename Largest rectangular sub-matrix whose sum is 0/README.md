<h2><a href="https://www.geeksforgeeks.org/problems/largest-rectangular-sub-matrix-whose-sum-is-0/1">Largest rectangular sub-matrix whose sum is 0</a></h2><hr><div><p>Given a matrix <strong>mat[][]</strong> of size <strong>N x M<strong>. The task is to find the largest rectangular sub-matrix by area whose sum is 0.
If there are multiple solutions return the rectangle which starts from minimum column index. If you still have multiple solutions return the one having greatest row number. If no such matrix is present return a zero (0) size matrix.</p>
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> N = 3, M = 3
mat[][] =  1, 2, 3
          -3,-2,-1
           1, 7, 5
<strong>Output:</strong> 1, 2, 3
        -3,-2,-1
<strong>Explanation:</strong> This is the largest sub-matrix, whose sum is 0.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> N = 4, M = 4
mat[][] = 9, 7, 16, 5
          1,-6,-7, 3
          1, 8, 7, 9
          7, -2, 0, 10
<strong>Output:</strong> -6,-7
          8, 7
         -2, 0 

<p>&nbsp;</p>
<p><strong>Your Task</strong></p>

<p>You don't need to read input or print anything. You just have to complete the function <strong>sumZeroMatrix()</strong> which takes a 2D matrix <strong>mat[][]</strong>, its dimensions <strong>N</strong> and <strong>M</strong> as inputs and returns a largest sub-matrix, whose sum is 0.</p>
<p><strong>Expected Time Complexity</strong>: O(N*M*M)
<strong>Expected Auxiliary Space</strong>: O(N*M)

<strong>Constraints</strong>:
1 ≤ N, M ≤ 100
-1000 ≤ mat[][] ≤ 1000

</div>
