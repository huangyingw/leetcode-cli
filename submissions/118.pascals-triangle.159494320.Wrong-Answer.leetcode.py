class Solution(object):
    def generate(self, numRows):
        result = []

        for i in range(numRows):
            result.append([1] * i)
        return result
