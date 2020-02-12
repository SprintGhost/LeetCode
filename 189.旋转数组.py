#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

# Accepted
# 34/34 cases passed (1116 ms)
# Your runtime beats 5.36 % of python3 submissions
# Your memory usage beats 49.49 % of python3 submissions (14.6 MB)

# @lc code=start
class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        need_move = k % len(nums)
        while (need_move):
            temp = nums[-1]
            nums[1:] = nums[:-1]
            nums[0] = temp
            need_move -= 1

class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        need_move = k % len(nums)
        nums = nums[::-1]
        nums[0:need_move] = nums[0:need_move][::-1]
        nums[need_move:] = nums[need_move:][::-1]
        # need_move = 1  for debug


# A = Solution()
# A.rotate([1,2,3,4,5,6,7], 3)
# @lc code=end

