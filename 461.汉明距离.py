#
# @lc app=leetcode.cn id=461 lang=python3
#
# [461] 汉明距离
#


# Accepted
# 149/149 cases passed (44 ms)
# Your runtime beats 39.3 % of python3 submissions
# Your memory usage beats 6.67 % of python3 submissions (13.7 MB)

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        temp = x ^ y
        index = 0
        while temp != 0:
            temp = temp & (temp - 1)
            index += 1
        return index
# @lc code=end

