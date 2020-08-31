#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#

# Accepted
# 276/276 cases passed (68 ms)
# Your runtime beats 91.47 % of python3 submissions
# Your memory usage beats 66.02 % of python3 submissions (13.7 MB)

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        step_1 = 0
        step_2 = 0
        for each in reversed(cost):
            temp = each + min(step_1, step_2)
            step_1 = step_2
            step_2 = temp
        return min(step_1,step_2)
    
        
# @lc code=end

