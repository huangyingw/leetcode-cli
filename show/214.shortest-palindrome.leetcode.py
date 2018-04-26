#
# [214] Shortest Palindrome
#
# https://leetcode.com/problems/shortest-palindrome/description/
#
# algorithms
# Hard (25.19%)
# Total Accepted:    53.3K
# Total Submissions: 211.5K
# Testcase Example:  '"aacecaaa"'
#
#
# Given a string S, you are allowed to convert it to a palindrome by adding
# characters in front of it. Find and return the shortest palindrome you can
# find by performing this transformation.
#
#
# For example:
# Given "aacecaaa", return "aaacecaaa".
# Given "abcd", return "dcbabcd".
#
# Credits:Special thanks to @ifanchu for adding this problem and creating all
# test cases. Thanks to @Freezen for additional test cases.
#


class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
