#
# [248] Strobogrammatic Number III
#
# https://leetcode.com/problems/strobogrammatic-number-iii/description/
#
# algorithms
# Hard (32.84%)
# Total Accepted:    11.6K
# Total Submissions: 35.3K
# Testcase Example:  '"50"\n"100"'
#
# A strobogrammatic number is a number that looks the same when rotated 180
# degrees (looked at upside down).
#
# Write a function to count the total strobogrammatic numbers that exist in the
# range of low <= num <= high.
#
# For example,
# Given low = "50", high = "100", return 3. Because 69, 88, and 96 are three
# strobogrammatic numbers.
#
# Note:
# Because the range might be a large number, the low and high numbers are
# represented as string.
#
#


class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
