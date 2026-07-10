class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(1,len(nums)):
            l1 = nums[:i]
            l2 = nums[i:]
            if (sum(l1) - sum(l2)) %2 == 0:
                count += 1

        return count