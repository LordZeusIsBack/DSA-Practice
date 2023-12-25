<h2><a href="https://www.geeksforgeeks.org/problems/candy/1">Candy</a></h2><h3>Medium</h3><hr><div><p>There are <strong>N</strong> children standing in a line. Each child is assigned a rating value given in the integer array <strong>ratings</strong>.
You are giving candies to these children subjected to the following requirements:</p>
<ul>
    <li>Each child must have atleast one candy.</li>
    <li>Children with a higher rating than its neighbors get more candies than their neighbors.</li></ul>
<p>Return the <strong>minimum</strong> number of candies you need to have to distribute.</p>
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> ratings = [1,0,2], N = 3
<strong>Output:</strong> 5
<strong>Explanation:</strong> You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> l1 = [1,2,2], N = 3
<strong>Output:</strong> 4
<strong>Explanation:</strong> You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it statisfies the above two conditions.
</pre>

<p>&nbsp;</p>
<p><strong>Your Task</strong></p>

<p>Your Task:
You don't need to read input or print anything. Your task is to complete the function minCandy() which takes the interger N and integer array ratings as parameters and returns the minimum number of candies you need to have to distribute.</p>
<p><strong>Expected Time Complexity</strong>: O(N)
<strong>Expected Auxiliary Space</strong>: O(N)

<strong>Constraints</strong>:
1 ≤ N ≤ 10^5
0 ≤ ratings ≤ 10^9

</div>
