#
# [302] Smallest Rectangle Enclosing Black Pixels
#
# https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/description/
#
# algorithms
# Hard (46.76%)
# Total Accepted:    17.4K
# Total Submissions: 37.2K
# Testcase Example:  '[["0","0","1","0"],["0","1","1","0"],["0","1","0","0"]]\n0\n2'
#
# An image is represented by a binary matrix with 0 as a white pixel and 1 as a
# black pixel. The black pixels are connected, i.e., there is only one black
# region. Pixels are connected horizontally and vertically. Given the location
# (x, y) of one of the black pixels, return the area of the smallest
# (axis-aligned) rectangle that encloses all black pixels.
#
#
# For example, given the following image:
#
# [
# ⁠ "0010",
# ⁠ "0110",
# ⁠ "0100"
# ]
#
# and x = 0, y = 2,
#
#
#
# Return 6.
#
#


class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
