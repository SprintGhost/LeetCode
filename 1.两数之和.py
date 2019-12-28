#
# @lc app=leetcode.cn id=1 lang=python3
#
#
#

# @lc code=start
class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None
        
# @lc code=end

