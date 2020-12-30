#
# @lc app=leetcode.cn id=1009 lang=python3
#
# [1009] 十进制整数的反码
#

# Accepted
# 128/128 cases passed (40 ms)
# Your runtime beats 51.87 % of python3 submissions
# Your memory usage beats 8.58 % of python3 submissions (14.8 MB)

# @lc code=start
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        temp = 1
        nums_temp = N >> 1
        while (nums_temp != 0):
            temp = (temp | (temp << 1))
            nums_temp = nums_temp >> 1
        return (N ^ temp)
# @lc code=end

