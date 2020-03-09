#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# Accepted
# 34/34 cases passed (52 ms)
# Your runtime beats 75.17 % of python3 submissions
# Your memory usage beats 15.32 % of python3 submissions (13.7 MB)

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        temp = dict()
        temp_1 = dict()
        for each in s:
            if each in temp:
                temp[each] += 1
            else:
                temp[each] = 0
        for each in t:
            if each in temp_1:
                temp_1[each] += 1
            else:
                temp_1[each] = 0
        return temp_1 == temp


# @lc code=end

