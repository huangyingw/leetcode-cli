#
# [356] Line Reflection
#
# https://leetcode.com/problems/line-reflection/description/
#
# algorithms
# Medium (30.29%)
# Total Accepted:    14.2K
# Total Submissions: 46.9K
# Testcase Example:  '[[1,1],[-1,1]]'
#
# Given n points on a 2D plane, find if there is such a line parallel to y-axis
# that reflect the given points.
#
#
# ⁠   Example 1:
#
#
# Given points = [[1,1],[-1,1]], return true.
#
#
#
# ⁠   Example 2:
#
#
# Given points = [[1,1],[-1,-1]], return false.
#
#
# Follow up:
# Could you do better than O(n2)?
#
#
# Credits:Special thanks to @memoryless for adding this problem and creating
# all test cases.
#


class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
