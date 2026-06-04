# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def dfs(root, curr_max):
            if not root:
                return 0
            if root.val >= curr_max:
                return dfs(root.left, root.val) + dfs(root.right, root.val) + 1
            return dfs(root.left, curr_max) + dfs(root.right, curr_max)
        return dfs(root, -101)