class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        nums1 = nums[:]          
        result = [0] * n

        for i in range(n):
            
            new_index = (i + nums1[i]) % n  
            result[i] = nums1[new_index]

        return result
