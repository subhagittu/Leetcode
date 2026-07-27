# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: int
        """
        def dfs(node):
            if not node:
                return 0
            current_val = 0
            if low <= node.val <= high:
                current_val = node.val

            return current_val + dfs(node.left) + dfs(node.right)


        return dfs(root)



