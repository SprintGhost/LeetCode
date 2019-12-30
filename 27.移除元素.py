#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#



# Accepted
# 113/113 cases passed (32 ms)
# Your runtime beats 96.5 % of python3 submissions
# Your memory usage beats 99.31 % of python3 submissions (12.7 MB)

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index_x = 0
        pre_len = len(nums)
        while(index_x < pre_len):
            if (nums[index_x]) == val:
                nums.pop(index_x)
                pre_len = len(nums)
            else:
                index_x += 1
        return index_x + 1
            
        
# @lc code=end

