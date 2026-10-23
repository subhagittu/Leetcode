class Solution(object):
    def sortPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = -1  
        for i, x in enumerate(nums):
            if x != i:  
                k &= x  
                if not k:  
                    return 0
        return max(k, 0)  