class Solution(object):
    def freqcount(self, ch1):
        d1 = {}
        for ele in ch1:
            if ele in d1:
                d1[ele] += 1
            else:
                d1[ele] = 1

        value_list = list(d1.values())
        for i in range(1,len(value_list)):
            if value_list[i] != value_list[i-1]:
                return False
        return True 



    def longestBalanced(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        res1 = ''
        maxres = ''
        for i in range(0,len(s)):
            res = ''
            res += s[i]
        
            for j in range(i+1,len(s)):
                res += s[j]
            
                if self.freqcount(res):
                    res1 = res
                    if len(res) > len(maxres):
                        maxres = res
            
        if len(s) == 1:
            return 1
        return len(maxres)




