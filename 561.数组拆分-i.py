#
# @lc app=leetcode.cn id=561 lang=python3
#
# [561] 数组拆分 I
#

# Accepted
# 81/81 cases passed (388 ms)
# Your runtime beats 34.5 % of python3 submissions
# Your memory usage beats 5.26 % of python3 submissions (16.2 MB)

# @lc code=start
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        index = 0
        nums_len = len(nums)
        result = 0
        while index < nums_len:
            result += nums[index]
            index += 2
        return result

# @lc code=end

