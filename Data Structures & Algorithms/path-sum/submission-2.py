# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.sum = 0
        def checkPath(root):
            if not root:
                return False
            self.sum += root.val
            if not root.left and not root.right and self.sum == targetSum:
                return True

            if checkPath(root.left):
                return True
            if checkPath(root.right):
                return True

            self.sum -= root.val
            return False
        return checkPath(root)
        