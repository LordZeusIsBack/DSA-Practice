<h2><a href="https://www.geeksforgeeks.org/problems/inorder-traversal-and-bst5855/1">Given an array <strong>arr</strong> of size <strong>N</strong>, determine whether this array represents an <strong>inorder traversal</strong> of a <strong>BST</strong>.

<strong>Note:</strong> All keys in BST must be unique.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> N = 3, arr = {2,4,5}
<strong>Output:</strong> 1
<strong>Explanation:</strong> Given array is inorder traversal for the following tree:
    4
   / \
  2   5</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> N = 3, arr = {2,4,1}
<strong>Output:</strong> 0
<strong>Explanation:</strong> Given array can not represent any BST.</pre>

<p>&nbsp;</p>
<p><strong>Your Task</strong></p>

<p>You don't need to read input or print anything. Your task is to complete the function <strong>isRepresentingBST()</strong> which takes the array <strong>arr[]</strong> and its size <strong>N</strong> as input parameters and returns 1 if array represents Inorder traversal of a BST, else returns 0.</p>
<p><strong>Expected Time Complexity</strong>: O(N)
<strong>Expected Auxiliary Space</strong>: O(1)

<strong>Constraints</strong>:
1 ≤ N ≤ 10^5
1 ≤ arr[i] ≤ 10^5

</div>
