#
# [191] Number of 1 Bits
#
# https://leetcode.com/problems/number-of-1-bits/description/
#
# algorithms
# Easy (40.49%)
# Total Accepted:    193.1K
# Total Submissions: 477K
# Testcase Example:  '           0 (00000000000000000000000000000000)'
#
# Write a function that takes an unsigned integer and returns the number of ’1'
# bits it has (also known as the Hamming weight).
#
# For example, the 32-bit integer ’11' has binary representation
# 00000000000000000000000000001011, so the function should return 3.
#
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
#


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
