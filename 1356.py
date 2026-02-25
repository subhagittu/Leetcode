class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        l2 = []
        
        d1 = {}
        for ele1 in arr:
            ele = ele1
            binary = ""
            if ele == 0:
                binary = '0'

            else:
                while ele > 0:
                    binary = str(ele%2) + binary
                    ele = ele//2
            d1[ele1] = int(binary.count('1'))

        l2 = sorted(arr, key=lambda x: (d1[x], x))
        

        return l2
        

             

        
