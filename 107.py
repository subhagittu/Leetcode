class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        res = []
        q = deque([root])
        
        while q:
            count = len(q)
            v = []
            
            for i in range(count):
                curr = q.popleft()
                
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                v.append(curr.val)
            
            res.append(v)
        
        res.reverse()
        return res