from collections import deque
class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        l1 = list(nums1)
        l2 = list(nums2)
        while l1 and l2:
            num1 = l1[0]
            num2 = l2[0]
            if num1 == num2:
                return num1
            if num1 < num2:
                l1.pop(0)
            if num1 > num2:
                l2.pop(0)

        return -1
        