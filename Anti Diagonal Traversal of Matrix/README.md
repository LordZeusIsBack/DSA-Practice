<h2><a href="https://www.geeksforgeeks.org/problems/print-diagonally1623/1">Anti Diagonal Traversal of Matrix</a></h2><hr><div><p>Give a N*N square <strong>matrix</strong>, return an array of its <strong>anti-diagonals</strong> in top-leftmost to bottom-rightmost order. In an element of a <strong>anti-diagonal (i, j)</strong>, surrounding elements will be <strong>(i+1, j-1)</strong> and <strong>(i-1, j+1)</strong>. Look at the examples for more clarity.</p>
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> N = 2, matrix[][] = 1 2
            3 4
<strong>Output:</strong> 1 2 3 4
<strong>Explanation:</strong> List of anti-diagnoals in order is
{1}, {2, 3}, {4}</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> N = 3, matrix[][] = 3 2 3
            4 5 1
            7 8 9
<strong>Output:</strong> 3 2 4 3 5 7 1 8 9
<strong>Explanation:</strong> List of anti-diagnoals in order is
{3}, {2, 4}, {3, 5, 7}, {1, 8}, {9}
</pre>
<p>&nbsp;</p>
<p><strong>Your Task</strong></p>

<p>You dont need to read input or print anything. Complete the function <strong>antiDiagonalPattern()</strong> that takes <strong>matrix</strong> as input parameter and returns a <strong>list of integers</strong> in order of the values visited in the anti-Diagonal pattern.</p>
<p><strong>Expected Time Complexity</strong>: O(N*N)
<strong>Expected Auxiliary Space</strong>: O(N*N)

<strong>Constraints</strong>:
1 ≤ N ≤ 100
0 ≤ mat[i][j] ≤ 100

</div>
