class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        flip = lambda x: '0' if x=='1' else '1'
        return ''.join(map(flip,[nums[i][i] for i in range(len(nums))]))
    
