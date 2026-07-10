class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        total_sum = sum(nums)
        leftsum = 0
        for i in range(0,len(nums)-1):
            leftsum += nums[i]
            rightsum = total_sum - leftsum

            if (leftsum %2) == (rightsum %2):
                count += 1

        return count