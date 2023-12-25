class Solution:
    def inOrderTraversal(self, root, lst):
        if root:
            self.inOrderTraversal(root.left, lst)
            lst.append(root.data)
            self.inOrderTraversal(root.right, lst)

    def reverseInOrderTraversal(self, root, lst):
        if root:
            self.reverseInOrderTraversal(root.right, lst)
            lst.append(root.data)
            self.reverseInOrderTraversal(root.left, lst)

    def countPairs(self, root1, root2, x):
        lst1 = []
        self.inOrderTraversal(root1, lst1)
        lst2 = []
        self.reverseInOrderTraversal(root2, lst2)
        count = 0
        i, j = 0, 0
        while i < len(lst1) and j < len(lst2):
            if lst1[i] + lst2[j] == x:
                count += 1
                i += 1
                j += 1
            elif lst1[i] + lst2[j] < x:
                i += 1
            else:
                j += 1

        return count