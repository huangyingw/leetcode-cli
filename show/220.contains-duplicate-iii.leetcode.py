#
# [220] Contains Duplicate III
#
# https://leetcode.com/problems/contains-duplicate-iii/description/
#
# algorithms
# Medium (18.77%)
# Total Accepted:    67.5K
# Total Submissions: 359.3K
# Testcase Example:  '[]\n0\n0'
#
# 
# Given an array of integers, find out whether there are two distinct indices i
# and j in the array such that the absolute difference between nums[i] and
# nums[j] is at most t and the absolute difference between i and j is at most
# k.
# 
#
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        