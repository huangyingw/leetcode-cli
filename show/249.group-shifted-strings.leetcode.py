#
# [249] Group Shifted Strings
#
# https://leetcode.com/problems/group-shifted-strings/description/
#
# algorithms
# Medium (44.39%)
# Total Accepted:    33.9K
# Total Submissions: 76.3K
# Testcase Example:  '["abc","bcd","acef","xyz","az","ba","a","z"]'
#
# Given a string, we can "shift" each of its letter to its successive letter,
# for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:
# "abc" -> "bcd" -> ... -> "xyz"
# 
# Given a list of strings which contains only lowercase alphabets, group all
# strings that belong to the same shifting sequence.
# 
# For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"], 
# A solution is:
# 
# [
# ⁠ ["abc","bcd","xyz"],
# ⁠ ["az","ba"],
# ⁠ ["acef"],
# ⁠ ["a","z"]
# ]
#
class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """