class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for n in nums:
            if n & 1:
                ans.append(n & ~(((n+1) & ~n) >> 1))
            else:
                ans.append(-1)
        return ans
        
