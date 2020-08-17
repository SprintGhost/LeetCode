#
# @lc app=leetcode.cn id=709 lang=python3
#
# [709] 转换成小写字母
#

# Accepted
# 8/8 cases passed (36 ms)
# Your runtime beats 85.13 % of python3 submissions
# Your memory usage beats 33.46 % of python3 submissions (13.7 MB)

# @lc code=start
class Solution:
    def toLowerCase(self, str: str) -> str:
        result = ""
        for each in str:
            if ((each >= "A") and (each <= "Z")):
                result += chr(ord(each) - ord("A") + ord("a"))
            else:
                result += each
                
        return result
        
# @lc code=end

