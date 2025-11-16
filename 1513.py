class Solution:
    def numSub(self, s: str) -> int:
        return sum(comb(len(t)+1,2) for t in s.split('0'))%(10**9+7)
