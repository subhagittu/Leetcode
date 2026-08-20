class Solution(object):
    def largestInteger(self, nums, k):
        freq = [0] * 51

        for num in nums:
            freq[num] += 1

        ans = -1
        n = len(nums)

        for i, num in enumerate(nums):

            if k == n:
                ans = max(ans, num)

            elif freq[num] == 1:

                if k == 1:
                    ans = max(ans, num)

                elif i == 0 or i == n - 1:
                    ans = max(ans, num)

        return ans