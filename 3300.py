class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = float('inf')
        for num in nums:
            digit_sum = 0

            while num > 0:
                digit_sum += num % 10
                num = num//10

            ans = min(ans, digit_sum)

        return ans
            
