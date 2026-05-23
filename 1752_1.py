class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums1 = nums[:]
        for i in range(0,len(nums)):
            nums1.append(nums1[0])
            nums1.pop(0)
            nums2 = nums1[:]
            if sorted(nums1) == nums1:
                return True
        return False

            


        
