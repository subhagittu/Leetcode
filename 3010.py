class Solution(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = nums[0]
        nums = nums[1:]
        nums.sort()
        return ans + nums[0] + nums[1]
        
