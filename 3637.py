class Solution(object):
    def isTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        peak = -1
        valley = n

        for i in range(n - 1):
            if peak == -1 and nums[i] >= nums[i + 1]:
                peak = i
            if valley == n and nums[-1 - i] <= nums[-2 - i]:
                valley = n - 1 - i
            if peak != -1 and valley != n:
                break

        if peak <= 0 or valley >= n - 1:
            return False

        for i in range(peak, valley):
            if nums[i] <= nums[i + 1]:
                return False

        return True
        
