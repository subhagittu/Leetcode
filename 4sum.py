class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        result = []
        self.helper(nums, target, 0, result, [], 4)
        return result

    def helper(self, nums, target, start, result, temp, num_need):
        if num_need != 2:
            for i in range(start, len(nums) - num_need + 1):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                temp.append(nums[i])
                self.helper(nums, target - nums[i], i + 1, result, temp, num_need - 1)
                temp.pop()
            return

        # Two pointer approach for base case (num_need == 2)
        l = start
        r = len(nums) - 1
        while l < r:
            total = nums[l] + nums[r]
            if total < target:
                l += 1
            elif total > target:
                r -= 1
            else:
                temp.append(nums[l])
                temp.append(nums[r])
                result.append(list(temp))
                temp.pop()
                temp.pop()
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
