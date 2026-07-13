class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        ans = []

        s = "123456789"
        l = str(low)
        h = str(high)

        for length in range(len(l), len(h) + 1):
            for start in range(0, 10 - length):
                num = int(s[start:start + length])
                if low <= num <= high:
                    ans.append(num)

        return ans

        