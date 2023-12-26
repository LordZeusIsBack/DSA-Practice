<h2><a href="https://www.geeksforgeeks.org/problems/rightmost-different-bit-1587115621/1">Rightmost different bit</a></h2><hr><div><p>Given two numbers <strong>M</strong> and <strong>N</strong>. The task is to find the position of the rightmost <strong>different</strong> bit in the binary representation of numbers. If both M and N are the same then return -1 in this case.</p>
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> M = 11, N = 9
<strong>Output:</strong> 2
<strong>Explanation:</strong> Binary representation of the given numbers are: 1011 and 1001, 2nd bit from right is different.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> M = 52, N = 4
<strong>Output:</strong> 5
<strong>Explanation:</strong> Binary representation of the given numbers are: 110100 and 0100, 5th-bit from right is different.</pre>

<p>&nbsp;</p>
<p><strong>Your Task</strong></p>

<p>The task is to complete the function <strong>posOfRightMostDiffBit()</strong> which takes two arguments <strong>M</strong> and <strong>N</strong> and returns the position of first different bits in M and N from right. If both m and n are the same then return -1 in this case.</p>
<p><strong>Expected Time Complexity</strong>: O(max(log M, log N))
<strong>Expected Auxiliary Space</strong>: O(1)

<strong>Constraints</strong>:
0 ≤ M
N ≤ 10^9

</div>
