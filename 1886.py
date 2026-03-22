class Solution(object):
    def findtranspose(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        transpose1 = [[0]*rows for _ in range(cols)]
        for i in range(0,len(mat)):
            for j in range(0,len(mat[i])):
                transpose1[j][i] = mat[i][j]

        return transpose1

    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        for _ in range(4):
            if mat == target:
                return True
            # Rotate 90 degrees clockwise
            mat = mat[::-1]
            mat = self.findtranspose(mat)
            #mat = [list(row) for row in zip(*mat[::-1])]
        return False
