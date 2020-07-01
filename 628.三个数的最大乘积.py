#
# @lc app=leetcode.cn id=628 lang=python3
#
# [628] 三个数的最大乘积
#

# Accepted
# 83/83 cases passed (336 ms)
# Your runtime beats 56.55 % of python3 submissions
# Your memory usage beats 20 % of python3 submissions (14.9 MB)

# @lc code=start
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        result = 1
        if len(nums) < 3:
            for each in nums:
                result = result * each
            return result
        nums = sorted(nums, reverse=True)
        return max(nums[0] * nums[1] * nums[2], nums[0] * nums[len(nums) - 1] * nums[len(nums) - 2])
# @lc code=end

