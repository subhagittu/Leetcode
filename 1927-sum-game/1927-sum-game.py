class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)

        q1 = q2 = 0
        s1 = s2 = 0

        for i in range(n // 2):
            if num[i] == '?':
                q1 += 1
            else:
                s1 += int(num[i])

        for i in range(n // 2, n):
            if num[i] == '?':
                q2 += 1
            else:
                s2 += int(num[i])

        if (q1 + q2) % 2:
            return True

        return 2 * (s1 - s2) != 9 * (q2 - q1)