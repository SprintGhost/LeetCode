#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# Accepted
# 18/18 cases passed (56 ms)
# Your runtime beats 95.9 % of python3 submissions
# Your memory usage beats 5 % of python3 submissions (20.3 MB)

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp = dict()
        # If use list, it will timeout
        for each in nums:
            if each not in temp:
                temp[each] = each
            else:
                return True
        return False
# @lc code=end

