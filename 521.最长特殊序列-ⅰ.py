#
# @lc app=leetcode.cn id=521 lang=python3
#
# [521] 最长特殊序列 Ⅰ
#

# Accepted
# 39/39 cases passed (40 ms)
# Your runtime beats 61.58 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13.7 MB)

# @lc code=start
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        return max(len(a), len(b))
# @lc code=end

