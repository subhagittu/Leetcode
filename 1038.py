# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.sum = 0
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        """
        Convert a Binary Search Tree (BST) to a Greater Sum Tree (GST).
        Uses reverse in-order traversal (right → root → left) to process nodes
        in descending order, maintaining a running sum and updating each node's
        value to be the cumulative sum of all nodes with values >= current node.
        """
        if root is not None:
            # Process right subtree first (larger values)
            self.bstToGst(root.right)
            
            # Update cumulative sum and node value
            self.sum += root.val
            root.val = self.sum
            
            # Process left subtree (smaller values)
            self.bstToGst(root.left)
        
        return root
