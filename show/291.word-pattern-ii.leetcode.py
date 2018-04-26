#
# [291] Word Pattern II
#
# https://leetcode.com/problems/word-pattern-ii/description/
#
# algorithms
# Hard (38.55%)
# Total Accepted:    22.3K
# Total Submissions: 57.9K
# Testcase Example:  '"abab"\n"redblueredblue"'
#
# Given a pattern and a string str, find if str follows the same pattern.
# ⁠Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty substring in str.
# 
# Examples:
# 
# pattern = "abab", str = "redblueredblue" should return true.
# pattern = "aaaa", str = "asdasdasdasd" should return true.
# pattern = "aabb", str = "xyzabcxzyabc" should return false.
# 
# 
# 
# 
# Notes:
# You may assume both pattern and str contains only lowercase letters.
# 
#
class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        
