class Solution(object):
    def maxDistance(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        i, j = 0, 1
        A = nums1
        B = nums2
        while i < len(A) and j < len(B):
            i += A[i] > B[j]
            j += 1

        return j - i - 1
