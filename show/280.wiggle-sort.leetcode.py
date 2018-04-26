#
# [280] Wiggle Sort
#
# https://leetcode.com/problems/wiggle-sort/description/
#
# algorithms
# Medium (58.69%)
# Total Accepted:    42.1K
# Total Submissions: 71.7K
# Testcase Example:  '[3,5,2,1,6,4]'
#
#
# Given an unsorted array nums, reorder it in-place such that nums[0] = nums[2]
# .
#
#
# For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6,
# 2, 5, 3, 4].
#
#


class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
