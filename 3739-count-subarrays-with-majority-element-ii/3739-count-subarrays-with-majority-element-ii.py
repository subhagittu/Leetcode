class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        freq = [0]*(2*n+1)
        less = 0
        ans = 0
        prev = n
        freq[prev] += 1
        for num in nums:
            if num == target:
                less += freq[prev]
                prev += 1
            else:
                prev -=1 
                less -= freq[prev]

            freq[prev] += 1
            ans += less

        return ans