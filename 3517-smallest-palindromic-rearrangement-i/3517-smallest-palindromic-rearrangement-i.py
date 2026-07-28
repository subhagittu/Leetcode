class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)

        d1 = Counter(s[:n//2])

        half = ''

        for char in 'abcdefghijklmnopqrstuvwxyz':
            if char in d1:
                half += char*d1[char]

        if n%2 == 1:
            middle = s[n//2]
        else:
            middle = ''

        return half + middle + half[::-1]