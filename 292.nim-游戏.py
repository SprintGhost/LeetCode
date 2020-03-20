#
# @lc app=leetcode.cn id=292 lang=python3
#
# [292] Nim 游戏
#

# Accepted
# 60/60 cases passed (40 ms)
# Your runtime beats 32.26 % of python3 submissions
# Your memory usage beats 5.01 % of python3 submissions (13.4 MB)

# @lc code=start
class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
        return n & 3 != 0
        
# @lc code=end

