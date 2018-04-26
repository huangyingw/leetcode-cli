#
# [189] Rotate Array
#
# https://leetcode.com/problems/rotate-array/description/
#
# algorithms
# Easy (25.35%)
# Total Accepted:    180.5K
# Total Submissions: 712.3K
# Testcase Example:  '[1,2,3,4,5,6,7]\n3'
#
# Rotate an array of n elements to the right by k steps.
#
# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to
# [5,6,7,1,2,3,4].
#
# Note:
# Try to come up as many solutions as you can, there are at least 3 different
# ways to solve this problem.
#
# [show hint]
#
# Hint:
# Could you do it in-place with O(1) extra space?
#
# Related problem: Reverse Words in a String II
#
# Credits:
# Special thanks to @Freezen for adding this problem and creating all test
# cases.
#
#


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
