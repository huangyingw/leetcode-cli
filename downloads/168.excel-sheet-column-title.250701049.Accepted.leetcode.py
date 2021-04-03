class Solution(object):
    def convertToTitle(self, n):
        result = ''
        while n:
            n -= 1
            result += chr(ord('A') + n % 26)
            n /= 26
        return result[::-1]

