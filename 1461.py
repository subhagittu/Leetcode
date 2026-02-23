class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        st = set()

        for i in range(len(s) - k + 1):
            st.add(s[i:i+k])

        return len(st) == 2**k
