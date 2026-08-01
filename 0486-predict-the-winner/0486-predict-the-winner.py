class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def solve(left, right):
            # Only one number left
            if left == right:
                return nums[left]

            # If I take the left number,
            # the opponent's advantage is solve(left+1, right)
            takeLeft = nums[left] - solve(left + 1, right)

            # If I take the right number,
            # the opponent's advantage is solve(left, right-1)
            takeRight = nums[right] - solve(left, right - 1)

            return max(takeLeft, takeRight)

        return solve(0, len(nums) - 1) >= 0