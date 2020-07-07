#
# @lc app=leetcode.cn id=504 lang=python3
#
# [504] 七进制数

# Accepted
# 241/241 cases passed (36 ms)
# Your runtime beats 77.14 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13.6 MB)#


# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        result = str()
        symbol =  1
        if (num < 7) and (num > -7):
            return str(num)
        if num < 0:
            symbol = -1
            num = num * -1
        while num > 0:
            result += str(num % 7)
            num = num // 7
        if symbol == -1:
            return "-" + result[::-1]
        else:
            return result[::-1]
        
# @lc code=end

