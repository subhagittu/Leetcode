class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        m = n
        
        m |= m >> 1
        m |= m >> 2
        m |= m >> 4
        m |= m >> 8
        m |= m >> 16
        
        if n==1 or n == 2:
            return (m+1)//2
        else:
            return (m+1)
        #return (m + 1) >> (3 // (n + 1))
