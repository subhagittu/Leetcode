class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        ans = []
        l1 = str(low)
        h1 = str(high)

        s1 = "123456789"

        for length in range(len(l1), len(h1)+1):
            for i in range(0,10-length):
                num = int(s1[i:i+length])
                if low <= num <= high:
                    ans.append(num)

        return ans

