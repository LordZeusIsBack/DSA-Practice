<h2><a href="https://www.geeksforgeeks.org/problems/check-whether-bst-contains-dead-end/1">Check whether BST contains Dead End</a></h2><h3>Medium</h3><hr><div><p>Given a Binary Search Tree that contains <strong>unique positive integer values greater than 0</strong>. The task is to complete the function <strong>isDeadEnd</strong> which returns <strong>true</strong> if the BST contains a <strong>dead end</strong> else returns <strong>false</strong>. Here <strong>Dead End</styrong> means a </strong>leaf</strong> node, at which no other node can be inserted.</p>
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong>               8
             /   \ 
           5      9
         /  \     
        2    7 
       /
      1     
<strong>Output:</strong> Yes
<strong>Explanation:</strong> Node 1 is a Dead End in the given BST.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong>               8
            /   \ 
           7     10
         /      /   \
        2      9     13
<strong>Output:</strong> 5
<strong>Explanation:</strong> Node 9 is a Dead End in the given BST.</pre>

<p>&nbsp;</p>
<p><strong>Your Task</strong></p>

<p>YYou don't have to input or print anything. Complete the function <strong>isDeadEnd()</strong> which takes <strong>BST</strong> as input and returns a boolean value.</p>
<p><strong>Expected Time Complexity</strong>: O(N)
<strong>Expected Auxiliary Space</strong>: O(N)

<strong>Constraints</strong>:
1 ≤ N ≤ 1001
1 ≤ Value of Nodes ≤ 10001

</div>
