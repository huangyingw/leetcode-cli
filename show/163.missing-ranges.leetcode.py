#
# [163] Missing Ranges
#
# https://leetcode.com/problems/missing-ranges/description/
#
# algorithms
# Medium (23.10%)
# Total Accepted:    38.8K
# Total Submissions: 168K
# Testcase Example:  '[0,1,3,50,75]\n0\n99'
#
# Given a sorted integer array nums, where the range of elements are in the
# inclusive range [lower, upper], return its missing ranges.
#
# Example:
#
#
# Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
# Output: ["2", "4->49", "51->74", "76->99"]
#
#
#


class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
