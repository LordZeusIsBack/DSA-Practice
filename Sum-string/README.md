<h2><a href="https://www.geeksforgeeks.org/problems/sum-string3151/1">Sum-string</a></h2><hr><div><p>Given a string of <strong>digits</strong>, the task is to check if it is a ‘<strong>sum-string</strong>’. A string <strong>S</strong> is called a sum-string when it is broken down into more than one substring and the rightmost substring can be written as a sum of two substrings before it and the same is recursively true for substrings before it.</p>
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> S = "12243660"
<strong>Output:</strong> 1
<strong>Explanation:</strong> "12243660" can be broken down as {"12", "24", "36", "60"}.
We can get 60 from 24 and 36 as 24 + 36 = 60. Similarly 36 can be written as 12 + 24.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> S = "1111112223"
<strong>Output:</strong> 1
<strong>Explanation:</strong> "1111112223" can be broken down as {"1", "111", "112", "223"}.
We can get 223 from 111 and 112 as 111 + 112 = 223. Similarly 112 can be written as 1 + 111..</pre>

<p>&nbsp;</p>
<p><strong>Your Task</strong></p>

<p>You don't need to read input or print anything. Your task is to complete the function <strong>isSumString()</strong> which takes the string S and returns 1 is S is a sum-string otherwise returns 0.</p>
<p><strong>Expected Time Complexity</strong>: O(|S|^3)
<strong>Expected Auxiliary Space</strong>: O(|S|)

<strong>Constraints</strong>:
1 ≤ |S| ≤ 500
String consists of characters from '0' to '9'.

</div>
