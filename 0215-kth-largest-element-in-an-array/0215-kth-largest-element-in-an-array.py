class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # nums.sort()
        # nums2 = []
        # for char in nums:
        #     if char not in nums2:
        #         nums2.append(char)

        nums.sort(reverse = True)
        k = k%len(nums)
        return nums[k-1]
