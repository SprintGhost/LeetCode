#
# @lc app=leetcode.cn id=747 lang=python3
#
# [747] 至少是其他数字两倍的最大数
#
# Accepted
# 250/250 cases passed (52 ms)
# Your runtime beats 47.33 % of python3 submissions
# Your memory usage beats 89.51 % of python3 submissions (13.5 MB)

# Accepted
# 250/250 cases passed (48 ms)
# Your runtime beats 71.71 % of python3 submissions
# Your memory usage beats 56.64 % of python3 submissions (13.6 MB)
# Tis result I modify the if judgment, 
# changed division to multiplication.
# @lc code=start
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        max_index = nums.index(max(nums))
        max_value = max(nums)
        nums.pop(max_index)
        if max(nums) * 2 <= max_value:
            return max_index
        return -1
        
# @lc code=end

