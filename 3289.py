class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        seen = [False] * n
        res = []
        for num in nums:
            if seen[num]:
                res.append(num)
            else:
                seen[num] = True
        if len(res) == 2 and res[0] > res[1]:
            res[0], res[1] = res[1], res[0]
        return res
