#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# Accepted
# 60/60 cases passed (32 ms)
# Your runtime beats 97.6 % of python3 submissions
# Your memory usage beats 28.57 % of python3 submissions (13.8 MB)

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        a = list(s)
        for i in range(0, len(a), 2*k):
            a[i:i+k] = reversed(a[i:i+k])
        return "".join(a)
# @lc code=end

