class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n, cnt=len(nums), 0
        freq=defaultdict(int)
        l=0
        for r, x in enumerate(nums):
            freq[x]+=1
            while freq[x]>k:
                freq[nums[l]]-=1
                l+=1
            cnt=max(cnt, r-l+1)
        return cnt