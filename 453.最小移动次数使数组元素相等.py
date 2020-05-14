#
# @lc app=leetcode.cn id=453 lang=python3
#
# [453] 最小移动次数使数组元素相等
#

# Accepted
# 84/84 cases passed (392 ms)
# Your runtime beats 29.88 % of python3 submissions
# Your memory usage beats 25 % of python3 submissions (15 MB)

# @lc code=start
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums = sorted(nums)
        index = len(nums) - 1
        result = 0
        while (index > 0):
            result += nums[index] - nums[0]
            index -= 1
        return result

# Accepted
# 84/84 cases passed (440 ms)
# Your runtime beats 18.5 % of python3 submissions
# Your memory usage beats 25 % of python3 submissions (14.9 MB)
        nums = sorted(nums)
        result = 0
        for index in range(1, len(nums)):
            diff = result + nums[index] - nums[index - 1]
            nums[index] += result
            result += diff
        return result

# Accepted
# 84/84 cases passed (364 ms)
# Your runtime beats 41.06 % of python3 submissions
# Your memory usage beats 25 % of python3 submissions (15 MB)
        nums = sorted(nums)
        result = 0
        for index in range(1, len(nums)):
            result += nums[index] - nums[0]
        return result
# @lc code=end

