class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size1 = len(nums)//2
        d1 = {}
        for i in nums:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1
        res = 0
        for i in d1:
            if d1[i] == size1:
                res = i
        return res

        
