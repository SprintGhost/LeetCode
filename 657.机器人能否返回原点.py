#
# @lc app=leetcode.cn id=657 lang=python3
#
# [657] 机器人能否返回原点
#
# Accepted
# 63/63 cases passed (68 ms)
# Your runtime beats 51.67 % of python3 submissions
# Your memory usage beats 16.67 % of python3 submissions (13.8 MB)
# @lc code=start
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x_axis = 0
        y_axis = 0
        for each in moves:
            if each == "R":
                x_axis += 1
            elif each == "L":
                x_axis -= 1
            elif each == "U":
                y_axis += 1
            else:
                y_axis -= 1
        return (x_axis == 0) and (y_axis == 0)
                
        
# @lc code=end

