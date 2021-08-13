'''
#73
https://leetcode.com/problems/set-matrix-zeroes/
'''
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        isZerothColZero, isZerothRowZero = False, False
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                isZerothColZero = True
                break

        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                isZerothRowZero = True
                break

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if isZerothColZero:
            for i in range(len(matrix)):
                matrix[i][0] = 0

        if isZerothRowZero:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0