#
# @lc app=leetcode.cn id=724 lang=python3
#
# [724] 寻找数组的中心索引
#
# Accepted
# 742/742 cases passed (52 ms)
# Your runtime beats 97.01 % of python3 submissions
# Your memory usage beats 55.58 % of python3 submissions (14.7 MB)
# @lc code=start
class Solution:
    def pivotIndex(self, nums) -> int:
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1

# @lc code=end

