#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#


# Accepted
# 201/201 cases passed (92 ms)
# Your runtime beats 21.71 % of python3 submissions
# Your memory usage beats 62.99 % of python3 submissions (14.4 MB)

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp_i_0 = 0
        dp_i_1 = -0xffffffff
        for index in range(len(prices)):
            temp = dp_i_0
            # sell
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[index])
            # buy 
            dp_i_1 = max(dp_i_1, temp-prices[index])
        return dp_i_0        
# @lc code=end

