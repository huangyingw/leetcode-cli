#
# [259] 3Sum Smaller
#
# https://leetcode.com/problems/3sum-smaller/description/
#
# algorithms
# Medium (42.00%)
# Total Accepted:    35.8K
# Total Submissions: 85.3K
# Testcase Example:  '[]\n0'
#
# Given an array of n integers nums and a target, find the number of index
# triplets i, j, k with 0  that satisfy the condition nums[i] + nums[j] +
# nums[k] < target.
#
# For example, given nums = [-2, 0, 1, 3], and target = 2.
#
# Return 2. Because there are two triplets which sums are less than 2:
#
# [-2, 0, 1]
# [-2, 0, 3]
#
#
# Follow up:
# Could you solve it in O(n2) runtime?
#
#


class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
