class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left = 0
        right = 0
        
        for i in range(1, n):
            if nums[i] < nums[left]:
                left = i
                
            if nums[i] > nums[right]:
                right = i
                
        if left < right:
            left, right = right, left
            
        ans = n
        
        for i in range(n + 1):
            extra = 0
            
            if right >= i:
                extra = n - right
            elif left >= i:
                extra = n - left
                
            ans = min(ans, i + extra)
            
        return ans