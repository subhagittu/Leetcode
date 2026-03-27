class Solution(object):
    def areSimilar(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: bool
        """
        k1 = 0
        mat1 = [row[:] for row in mat]
        while k1 < k:
            
            for i,rows in enumerate(mat1):
                if i%2 == 0:
                    l1 = rows[:]
                    l1.append(l1[0])
                    l1.pop(0)
                    rows[:] = l1[:]

                else:
                    num1 = rows[-1]
                    l1 = rows[:]
                    l1.insert(0,num1)
                    l1.pop(-1)
                    rows[:] = l1[:]

            k1 += 1

        if mat1 == mat:
            return True
        else:
            return False

        

        
