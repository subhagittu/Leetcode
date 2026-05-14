class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums) - 1
        dup = 0

        for num in nums:
            val = abs(num)
            if val > n: return False

            if nums[val - 1] < 0:
                if val < n or dup: return False
                dup |= 1
                continue

            nums[val - 1] = -nums[val - 1]

        return True
