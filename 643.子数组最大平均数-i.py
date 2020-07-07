#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#
# Time Limit Exceeded
# 115/123 cases passed (N/A)
# Accepted
# 123/123 cases passed (1240 ms)
# Your runtime beats 19.09 % of python3 submissions
# Your memory usage beats 10 % of python3 submissions (17.3 MB)
# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        result = temp = sum(nums[0:k])
        index = k
        while index < len(nums):
            temp += nums[index] - nums[index - k]
            result = max(temp, result)
            index += 1
        return result / k

        
# @lc code=end

