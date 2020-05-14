#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#


# Accepted
# 54/54 cases passed (76 ms)
# Your runtime beats 5.94 % of python3 submissions
# Your memory usage beats 5.66 % of python3 submissions (13.6 MB)

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        temp = dict()
        for each in s:
            if each in temp:
                temp[each] += 1
            else:
                temp[each] = 1
        for each in t:
            if each not in temp:
                return each
            else:
                temp[each] -= 1
        for each in temp:
            if temp[each] < 0:
                return each


# A = Solution()
# A.findTheDifference("a","aa")
        
# @lc code=end

