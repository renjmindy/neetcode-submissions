# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def help(self, root):

        if not root: return 0

        self.ans = max(self.ans, self.help(root.left) + self.help(root.right))

        return 1 + max(self.help(root.left), self.help(root.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.ans = 0

        self.help(root)

        return self.ans
        