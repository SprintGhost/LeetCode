#
# @lc app=leetcode.cn id=665 lang=python3
#
# [665] 非递减数列
# Accepted
# 325/325 cases passed (56 ms)
# Your runtime beats 52.53 % of python3 submissions
# Your memory usage beats 33.33 % of python3 submissions (14.8 MB)#

# @lc code=start
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        index = 1
        n = len(nums)
        flag = 0
        while (index <= n - 1) and (flag < 2):
            if nums[index - 1] > nums[index]:
                flag += 1
                if (index - 2 >= 0) and (nums[index - 2] > nums[index]):
                    nums[index] = nums[index - 1]
            index += 1

        return (flag < 2)
            

# @lc code=end

