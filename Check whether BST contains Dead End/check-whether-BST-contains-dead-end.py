class Solution:
    def helper(self, node, MIN, MAX):
        if not node:
            return False

        if node.data == MIN and node.data == MAX:
            return True

        return (
            self.helper(node.left, MIN, node.data - 1)
            or self.helper(node.right, node.data + 1, MAX)
        )

    def isDeadEnd(self, root):
        return self.helper(root, 1, 10 ** 8)