#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# Accepted
# 23/23 cases passed (56 ms)
# Your runtime beats 95.54 % of python3 submissions
# Your memory usage beats 31.16 % of python3 submissions (21.2 MB)

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        temp= dict()
        for index, each in enumerate(nums):
            if each in temp:
                if (index - temp[each]) <= k:
                    return True
                else:
                    temp[each] = index
            else:
                temp[each] = index
        return False
            
        
# @lc code=end

