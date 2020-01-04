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


# Double pointer solution 
# 113/113 cases passed (40 ms)
# Your runtime beats 76.51 % of python3 submissions
# Your memory usage beats 99.31 % of python3 submissions (12.8 MB)

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index_x = 0
        index_y = 0
        pre_len = len(nums)
        while(index_y < pre_len):
            if (nums[index_y]) != val:
                nums[index_x] = nums[index_y]
                index_x += 1
            index_y += 1
        return index_x
        
# @lc code=end

