#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# Accepted
# 21/21 cases passed (48 ms)
# Your runtime beats 80.19 % of python3 submissions
# Your memory usage beats 11.99 % of python3 submissions (14 MB)

# @lc code=start
class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
            # nums[0]~nums[lastNonZeroIndex]!=0
        lastNonZeroIndex = -1
        nums_length = len(nums)
        for index in range(0, nums_length):
            if (nums[index] != 0):
                lastNonZeroIndex += 1
                nums[lastNonZeroIndex] = nums[index]
                if (index != lastNonZeroIndex):
                    nums[index] = 0
            

# A = Solution()
# A.moveZeroes([0,1,0,3,12])
# @lc code=end

