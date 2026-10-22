class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        want = list(range(n))
        i = nums.index(0)
        if nums[i:] + nums[:i] == want:
            return min(i, n - i + 2)
        if nums[i::-1] + nums[:i:-1] == want:
            return min(i + 2, n - i)
        return -1