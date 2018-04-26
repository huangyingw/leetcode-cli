#
# [836] Race Car
#
# https://leetcode.com/problems/race-car/description/
#
# algorithms
# Hard (26.67%)
# Total Accepted:    1.6K
# Total Submissions: 6K
# Testcase Example:  '3'
#
# Your car starts at position 0 and speed +1 on an infinite number line.  (Your
# car can go into negative positions.)
#
# Your car drives automatically according to a sequence of instructions A
# (accelerate) and R (reverse).
#
# When you get an instruction "A", your car does the following: position +=
# speed, speed *= 2.
#
# When you get an instruction "R", your car does the following: if your speed
# is positive then speed = -1 , otherwise speed = 1.  (Your position stays the
# same.)
#
# For example, after commands "AAR", your car goes to positions 0->1->3->3, and
# your speed goes to 1->2->4->-1.
#
# Now for some target position, say the length of the shortest sequence of
# instructions to get there.
#
#
# Example 1:
# Input:
# target = 3
# Output: 2
# Explanation:
# The shortest instruction sequence is "AA".
# Your position goes from 0->1->3.
#
#
#
# Example 2:
# Input:
# target = 6
# Output: 5
# Explanation:
# The shortest instruction sequence is "AAARA".
# Your position goes from 0->1->3->7->7->6.
#
#
#
#
# Note:
#
#
# 1 <= target <= 10000.
#
#


class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
