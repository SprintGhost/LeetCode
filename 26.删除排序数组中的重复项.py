#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#


# Accepted
# 161/161 cases passed (108 ms)
# Your runtime beats 60.51 % of python3 submissions
# Your memory usage beats 99.15 % of python3 submissions (14.4 MB)

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pre_len = len(nums)
        index = 1
        while (index < pre_len):
            if (nums[index -1 ] == nums[index]):
                nums.pop(index)
                pre_len = pre_len - 1
            else:
                index = index + 1
        return index
        
# @lc code=end

