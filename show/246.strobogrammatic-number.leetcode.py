#
# [246] Strobogrammatic Number
#
# https://leetcode.com/problems/strobogrammatic-number/description/
#
# algorithms
# Easy (40.29%)
# Total Accepted:    35.4K
# Total Submissions: 87.8K
# Testcase Example:  '"69"'
#
# A strobogrammatic number is a number that looks the same when rotated 180
# degrees (looked at upside down).
#
# Write a function to determine if a number is strobogrammatic. The number is
# represented as a string.
#
# For example, the numbers "69", "88", and "818" are all strobogrammatic.
#
#


class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
