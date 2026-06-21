class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        cn=0
        costs.sort()
        for i in costs:
            if i<=coins:
                cn+=1
                coins-=i
        return cn
 
