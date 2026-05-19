from collections import deque
class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        queue1 = deque(nums1)
        queue2 = deque(nums2)
        
        
        while queue1 and queue2:
            head1 = queue1[0]
            head2 = queue2[0]
            
            if head1 == head2:
                return head1  
            elif head1 < head2:
                queue1.popleft()  
            else:
                queue2.popleft() 
                
        return -1
