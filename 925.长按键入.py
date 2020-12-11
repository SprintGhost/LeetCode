#
# @lc app=leetcode.cn id=925 lang=python3
#
# [925] 长按键入
#
# Accepted
# 84/84 cases passed (40 ms)
# Your runtime beats 65.46 % of python3 submissions
# Your memory usage beats 32.83 % of python3 submissions (13.6 MB)
# @lc code=start
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        index_name = 0
        index_typed = 0
        while index_typed < len(typed):
            if (index_name < (len(name))) and (name[index_name] == typed[index_typed]):
                index_name += 1
                index_typed += 1
            elif (index_typed > 0) and (typed[index_typed - 1] == typed[index_typed]):
                index_typed += 1
            else:
                return False
        return (index_name == len(name))
             
# @lc code=end

