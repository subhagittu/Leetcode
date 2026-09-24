class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i, x in enumerate(nums):
            digitSum=0
            while x>0:
                x, r=divmod(x, 10)
                digitSum+=r
            if digitSum==i: return i
        return -1     
