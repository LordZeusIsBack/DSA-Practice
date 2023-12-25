<h2><a href="https://www.geeksforgeeks.org/problems/minimize-the-heights3351/1">Minimize the Heights II</a></h2><h3>Medium</h3><hr><div><p>Given an array <strong>arr[]</strong> denoting heights of <strong>N</strong> towers and a positive integer <strong>K</strong>.
For <strong>each</strong> tower, you must perform <strong>exactly one</strong> of the following operations <strong>exactly once</strong>.</p>
<ul>
    <li><strong>Increase</strong> the height of the tower by <strong>K</strong></li>
    <li><strong>Decrease</strong> the height of the tower by <strong>K</strong></li></ul>
<p>Find out the <strong>minimum</strong> possible difference between the height of the shortest and tallest towers after you have modified each tower.
You can find a slight modification of the problem here.
Note: It is compulsory to increase or decrease the height by K for each tower. After the operation, the resultant array should not contain any negative integers.</p>
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> K = 3, N = 5, Arr[] = {3, 9, 12, 16, 20}
<strong>Output:</strong> 11
<strong>Explanation:</strong> The array can be modified as
{3+k, 9+k, 12-k, 16-k, 20-k} -> {6, 12, 9, 13, 17}. 
The difference between 
the largest and the smallest is 17-6 = 11.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> K = 2, N = 4, Arr[] = {1, 5, 8, 10}
<strong>Output:</strong> 5
<strong>Explanation:</strong> The array can be modified as 
{1+k, 5-k, 8-k, 10-k} = {3, 3, 6, 8}. 
The difference between 
the largest and the smallest is 8-3 = 5.
</pre>

<p>&nbsp;</p>
<p><strong>Your Task</strong></p>

<p>You don't need to read input or print anything. Your task is to complete the function <strong>getMinDiff()</strong> which takes the <strong>arr[]</strong>, <strong>n</strong>, and <strong>k</strong> as input parameters and returns an integer denoting the minimum difference.</p>
<p><strong>Expected Time Complexity</strong>: O(N*logN)
<strong>Expected Auxiliary Space</strong>: O(N)

<strong>Constraints</strong>:
1 ≤ K ≤ 10^9
1 ≤ N ≤ 10^5
0 ≤ Arr[i] ≤ 10^9

</div>
