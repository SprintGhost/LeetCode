#
# @lc app=leetcode.cn id=441 lang=python3
#
# [441] 排列硬币
#

# Accepted
# 1336/1336 cases passed (1088 ms)
# Your runtime beats 28.62 % of python3 submissions
# Your memory usage beats 33.33 % of python3 submissions (13.7 MB)

# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        index = 0
        while(n - index > 0):
            index += 1
            n = n - index
        return index
        return int((0.25+2*n)**0.5-0.5)

# A = Solution()
# A.arrangeCoins(5)
# @lc code=end

