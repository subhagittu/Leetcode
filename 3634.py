class Solution(object):
    def minRemoval(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        max_len = 0
        i = 0
        for j in range(0,len(nums)):
            while nums[i]*k < nums[j]:
                i += 1
            max_len = max(max_len,j-i+1)

        return len(nums)-max_len 
