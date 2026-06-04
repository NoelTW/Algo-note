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
            nonlocal ans
            if not root:
                return
            # pre-order
            print(root.val)
            if root.val >= curr_max:
                ans += 1
                curr_max = root.val
            dfs(root.left, curr_max)
            dfs(root.right, curr_max)

        dfs(root, -101)
        return ans

        """
            3
          3
        4   2

        """
