#
# @lc app=leetcode.cn id=645 lang=python3
#
# [645] 错误的集合
#

# Accepted
# 49/49 cases passed (216 ms)
# Your runtime beats 99.61 % of python3 submissions
# Your memory usage beats 50 % of python3 submissions (15.3 MB)

# @lc code=start
class Solution:
    def findErrorNums(self, nums):
        nums_sum = sum(nums)
        max_number = len(nums)
        nums_sum_true = (max_number * max_number + max_number) // 2
        temp = nums_sum_true - nums_sum
        temp_dict = dict()
        for each in nums:
            if each not in temp_dict:
                temp_dict[each] = 0
            else:
                return [each, each + temp]

# A = Solution()
# A.findErrorNums([1,1])
# @lc code=end

