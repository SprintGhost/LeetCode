#
# @lc app=leetcode.cn id=459 lang=python3
#
# [459] 重复的子字符串
#

# Accepted
# 120/120 cases passed (44 ms)
# Your runtime beats 81.01 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13.8 MB)

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s).find(s,1) != len(s)
        
# @lc code=end

