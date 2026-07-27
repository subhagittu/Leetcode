# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        res = []
        if not root:
            return res

        q = deque()
        q.append(root)

        while q:
            #l1 = []
            sum1 = 0
            count = 0
            for _ in range(len(q)):
                node = q.popleft()
                #l1.append(node.val)
                sum1 += node.val
                count += 1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            avg_num = float(sum1)/count
            res.append(avg_num)

        return res