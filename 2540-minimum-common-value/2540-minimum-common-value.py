from collections import deque
class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        queue1 = list(nums1)
        queue2 = list(nums2)
        while queue1 and queue2:
            num1 = queue1[0]
            num2 = queue2[0]
            if num1 == num2:
                return num1
            if num1 < num2:
                queue1.pop(0)
            if num1 > num2:
                queue2.pop(0)

        return -1
        