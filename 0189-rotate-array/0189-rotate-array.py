class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k1 = len(nums)-k
        k1 = k1%len(nums)
        for i in range(0,k1):
            nums.append(nums[0])
            nums.pop(0)

        
