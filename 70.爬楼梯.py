#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# Accepted
# 45/45 cases passed (24 ms)
# Your runtime beats 98.33 % of python3 submissions
# Your memory usage beats 70.08 % of python3 submissions (13.1 MB)

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        first = 1
        second = 2
        index = 3
        while (index <= n):
            third = first + second
            first = second
            second = third
            index += 1
        return second
# @lc code=end

