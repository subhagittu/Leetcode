class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i,ele in enumerate(nums):
            if target-ele in nums:
                index1 = nums.index(target-ele)
                if i != index1:
                    return [i,index1]