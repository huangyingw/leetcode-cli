class Solution(object):
    def setZeroes(self, matrix):
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[row][0] = '#'
                    matrix[0][col] = '#'
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == '#':
                    matrix[row][col] = 0:

