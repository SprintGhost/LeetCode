#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# Accepted
# 69/69 cases passed (28 ms)
# Your runtime beats 93.07 % of python3 submissions
# Your memory usage beats 43.42 % of python3 submissions (13 MB)

# @lc code=start
class Solution:
    def rob(self, nums) -> int:
        pre_sum = 0
        curr_sum = 0 
        for each in nums:
            temp = curr_sum
            curr_sum = max(pre_sum + each, curr_sum)
            pre_sum = temp
        return curr_sum
            
# A = Solution()
# A.rob([2,1,1,2])

# @lc code=end

