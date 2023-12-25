<h2><a href="https://www.geeksforgeeks.org/problems/inorder-traversal-and-bst5855/1">Brothers From Different Roots</a></h2><hr><div><p>Given two BSTs containing <strong>N1</strong> and <strong>N2</strong> distinct nodes respectively and given a value <strong>x</strong>, your task is to complete the function <strong>countPairs()</strong>, that returns the count of all pairs of (a, b), where <strong>a</strong> belongs to one BST and <strong>b</strong> belongs to another BST, such that <strong>a + b = x</strong>.</p>
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> x = 16, BST1:        5
     /   \
    3     7
   / \   / \
  2   4 6   8

BST2: 10
/ \
 6 15
/ \ / \
 3 8 11 18
<strong>Output:</strong> 3
<strong>Explanation:</strong> The pairs are: (5, 11), (6, 10) and (8, 8)</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> x = 4, BST1:   1
   \
    3
   /
  2

  BST2:     3
   / \
  2   4
 /     
1
<strong>Output:</strong> 3
<strong>Explanation:</strong> The pairs are: (2, 2), (3, 1) and (1, 3).</pre>

<p>&nbsp;</p>
<p><strong>Your Task</strong></p>

<p>You don't need to read input or print anything. Your task is to complete the function <strong>countPairs()</strong>, which takes <strong>two BST's</strong> as parameter in the form of <strong>root1 and root2</strong> and the integer <strong>x</strong>, that returns the count of all pairs from both the <strong>BSTs</strong> whose sum is equal to x.</p>
<p><strong>Expected Time Complexity</strong>: O(N)
<strong>Expected Auxiliary Space</strong>: O(N)

<strong>Constraints</strong>:
1 ≤ Number of nodes ≤ 10^5
1 ≤ Data of a node ≤ 10^6

</div>
