class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        min_val, max_val = nums[0], nums[-1]
        
        return self.gcd(min_val, max_val)
        
    def gcd(self, a: int, b: int) -> int:
        while b != a:
            if b >= a:
                b -= a
            else:
                a -= b
        return a
        
