# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0

        q = deque()
        q.append(root)
        level = 0
        l1 = []
        while q:
            level_size = len(q)
            level_sum = 0
            #print(f"Level {level}:",end = ' ')
        
            for _ in range(level_size):
                curr = q.popleft()
                
                level_sum += curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            
            l1.append(level_sum)
        max1 = float('-inf')
        for i in l1:
            max1 = max(max1,i)

        for i in range(0,len(l1)):
            if max1 ==l1[i]:
                return i+1 

        

                
        
