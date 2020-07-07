#
# @lc app=leetcode.cn id=575 lang=python3
#
# [575] 分糖果
#

# Accepted
# 205/205 cases passed (1020 ms)
# Your runtime beats 75.47 % of python3 submissions
# Your memory usage beats 33.33 % of python3 submissions (15.3 MB)

# @lc code=start
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        temp = dict()
        for each in candies:
            if each in temp:
                temp[each] += 1
            else:
                temp[each] = 1
        
        return min(len(temp), len(candies) // 2)
        
# @lc code=end

