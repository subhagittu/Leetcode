class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        x = 0
        for n in nums:
            if not (n % k):
                i = (n // k) - 1
                x |= 1 << i

        return ((x + 1) & ~x).bit_length() * k