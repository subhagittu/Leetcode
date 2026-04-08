import numpy as np
class Solution(object):
    def xorAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        arr = np.array(nums, dtype=np.int64)
        MOD = 10**9 + 7

        for li, ri, ki, vi in queries:
            
            arr[li : ri + 1 : ki] = (arr[li : ri + 1 : ki] * vi) % MOD

        
        return int(np.bitwise_xor.reduce(arr))
