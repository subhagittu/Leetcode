class Solution(object):
    def resultArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = [0] * k
        state = [0] * k
        for value in nums:
            rem = value % k
            next_state = [0] * k
            for r in range(k):
                product_rem = (r * rem) % k
                next_state[product_rem] += state[r]
                result[product_rem] += state[r]
            next_state[rem] += 1
            result[rem] += 1
            state = next_state
        return result