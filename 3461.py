class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s = list(s)
        length = len(s)
        while length > 2:
            for i in range(length - 1):
                s[i] = str((int(s[i]) + int(s[i+1])) % 10)
            length -= 1
        return s[0] == s[1]
