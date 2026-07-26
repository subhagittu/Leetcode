# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def is_mirror(p,q):
            if p is None and q is None:
                return True
        
            if p is None or q is None:
                return False
       
            if p.val == q.val:
                return is_mirror(p.left, q.right) and is_mirror(p.right, q.left)
        
            return False

        return is_mirror(root.left, root.right)

