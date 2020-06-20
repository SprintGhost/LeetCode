#
# @lc app=leetcode.cn id=594 lang=python3
#
# [594] 最长和谐子序列
#

# Accepted
# 201/201 cases passed (520 ms)
# Your runtime beats 17.97 % of python3 submissions
# Your memory usage beats 33.33 % of python3 submissions (15.3 MB)

# @lc code=start
class Solution:
    def findLHS(self, nums) -> int:
        has_temp = dict()
        result = 0
        temp_low = 0
        temp_high = 0
        for each in nums:
            if each not in has_temp:
                has_temp[each] = 1
            else:
                has_temp[each] += 1
            if each - 1 in has_temp:
                temp_low = has_temp[each -1 ] + has_temp[each]
            if each + 1 in has_temp:
                temp_high = has_temp[each + 1] + has_temp[each]
            temp_high = max(temp_high,temp_low)
            result = max(temp_high, result)
        
        return result

            
        
# @lc code=end

