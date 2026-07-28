class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)

        # Count characters in the first half
        freq = Counter(s[:n // 2])

        half = ""

        # Add characters in alphabetical order
        for ch in "abcdefghijklmnopqrstuvwxyz":
            if ch in freq:
                half += ch * freq[ch]

        # Middle character (only for odd length)
        if n % 2 == 1:
            middle = s[n // 2]
        else:
            middle = ""

        # Build palindrome
        return half + middle + half[::-1]