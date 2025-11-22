class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        min1 = 0
        for i in nums:
            z = i
            if z%3 != 0:
                k = z
                j = z
                count1 = 0
                count2 = 0
                while k%3!=0:
                    k+=1
                    count1+=1
                while j%3!=0:
                    j-=1
                    count2+=1
                min1 = min(count1,count2)
                res += min1
        return res


        
