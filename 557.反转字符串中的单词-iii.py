#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#

# Accepted
# 30/30 cases passed (44 ms)
# Your runtime beats 75.21 % of python3 submissions
# Your memory usage beats 7.14 % of python3 submissions (14 MB)

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        result = ""
        for each in s:
            result += each[::-1] + " "
        return result[:len(result) - 1]
        
# @lc code=end

