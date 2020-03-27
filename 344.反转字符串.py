#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#

# Accepted
# 478/478 cases passed (48 ms)
# Your runtime beats 89.25 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (14.7 MB)

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s_len = len(s)
        index = 0
        while index < s_len:
            temp = s[index]
            s[index] = s[s_len - 1]
            s[s_len - 1] = temp
            index += 1
            s_len -= 1
# @lc code=end

