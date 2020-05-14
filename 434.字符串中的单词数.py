#
# @lc app=leetcode.cn id=434 lang=python3
#
# [434] 字符串中的单词数
#

# Accepted
# 26/26 cases passed (32 ms)
# Your runtime beats 83.37 % of python3 submissions
# Your memory usage beats 50 % of python3 submissions (13.5 MB)

# @lc code=start
class Solution:
    def countSegments(self, s: str) -> int:
        result = 0
        temp = False
        # if s == "":
        #     return 0
        for each in s:
            if each == " ":
                if temp:
                    temp = False
            else:
                if not temp:
                    result += 1
                    temp = True
        return result
        
# @lc code=end

