class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d1 = {}
        for ele in strs:
            key = ''.join(sorted(ele))
            if key in d1:
                d1[key].append(ele)
            else:
                d1[key] = [ele]
        l1 = []
        for key,values in d1.items():
            l1.append(values)

        sorted(l1,key = len)
        return l1