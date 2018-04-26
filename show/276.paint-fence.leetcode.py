#
# [276] Paint Fence
#
# https://leetcode.com/problems/paint-fence/description/
#
# algorithms
# Easy (34.86%)
# Total Accepted:    32.3K
# Total Submissions: 92.7K
# Testcase Example:  '0\n0'
#
#
# There is a fence with n posts, each post can be painted with one of the k
# colors.
# You have to paint all the posts such that no more than two adjacent fence
# posts have the same color.
# Return the total number of ways you can paint the fence.
#
# Note:
# n and k are non-negative integers.
#


class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
