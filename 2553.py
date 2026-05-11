class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l1 = []
        for ele in nums:
            str1 = str(ele)
            n = 0
            while n < len(str1):
                l1.append(int(str1[n]))
                n += 1

        return l1
