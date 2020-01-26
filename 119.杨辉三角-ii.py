#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# Accepted
# 34/34 cases passed (32 ms)
# Your runtime beats 84.15 % of python3 submissions
# Your memory usage beats 67.72 % of python3 submissions (13.1 MB)

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # if rowIndex == 0: return [1]
        res = [1]
        while len(res) < (rowIndex + 1):
            res = [a+b for a, b in zip([0]+res, res+[0])]      
        return res
# @lc code=end

