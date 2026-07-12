class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(0,len(nums)-3):
            for j in range(i+1, len(nums)-2):
                left = j+1
                right = len(nums)-1
                while left < right:
                    if nums[i] + nums[j] + nums[left] + nums[right] > target:
                        right -= 1
                    elif nums[i] + nums[j] + nums[left] + nums[right] < target:
                        left += 1

                    else:
                        l1 = [nums[i],nums[j],nums[left],nums[right]]
                        if l1 not in res:
                            res.append(l1)
                        left += 1
                        right -= 1


        return res