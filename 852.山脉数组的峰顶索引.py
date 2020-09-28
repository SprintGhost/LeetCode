#
# @lc app=leetcode.cn id=852 lang=python3
#
# [852] 山脉数组的峰顶索引
#
# 34/34 cases passed (56 ms)
# Your runtime beats 82.66 % of python3 submissions
# Your memory usage beats 98.9 % of python3 submissions (14.2 MB)
# @lc code=start
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        max_number = max(arr)
        return arr.index(max_number)
# @lc code=end

