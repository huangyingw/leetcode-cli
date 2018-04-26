#
# [409] Longest Palindrome
#
# https://leetcode.com/problems/longest-palindrome/description/
#
# algorithms
# Easy (46.00%)
# Total Accepted:    63.7K
# Total Submissions: 138.6K
# Testcase Example:  '"abccccdd"'
#
# Given a string which consists of lowercase or uppercase letters, find the
# length of the longest palindromes that can be built with those letters.
# 
# This is case sensitive, for example "Aa" is not considered a palindrome
# here.
# 
# Note:
# Assume the length of given string will not exceed 1,010.
# 
# 
# Example: 
# 
# Input:
# "abccccdd"
# 
# Output:
# 7
# 
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
# 
# 
#
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        
