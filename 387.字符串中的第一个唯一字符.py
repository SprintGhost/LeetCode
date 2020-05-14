#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# Accepted
# 104/104 cases passed (108 ms)
# Your runtime beats 75.32 % of python3 submissions
# Your memory usage beats 5.41 % of python3 submissions (13.7 MB)

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        temp = dict()
        for index, each in enumerate(s):
            if each in temp:
                temp[each] = -1
            else:
                temp[each] = index
        for each in temp:
            if temp[each] != -1:
                return temp[each]
        return -1
        
# @lc code=end

