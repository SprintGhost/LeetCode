#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        number_flag = 1
        if (x < 0):
            number_flag = -1
        x = number_flag * int((str(x * number_flag)[::-1]))
        if (x < -2**31) or (x > (2**31 - 1)):
            return 0
        return x
        
# @lc code=end

