class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def maxDiff(i, j):
            if i == j: return nums[i]
            return max(nums[i] - maxDiff(i + 1, j),
                       nums[j] - maxDiff(i, j - 1))

        return maxDiff(0, len(nums) - 1) >= 0