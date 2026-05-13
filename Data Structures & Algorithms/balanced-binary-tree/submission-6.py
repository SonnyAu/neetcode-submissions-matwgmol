# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        '''
        step 1: set up our dfs template
        step 2: for the return at the leaf nodes, return [True, 0]
        step 3: at every node, take the left and right states and check
        if the heights are <= 1
        step 4: move state up tree ([result of check, 1 + max(left[1], right[1])])
        step 5: return dfs(root)[0]
        '''
        def dfs(root):
            if not root:
                return [True, 0]
            
            left, right = dfs(root.left), dfs(root.right)

            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]











        