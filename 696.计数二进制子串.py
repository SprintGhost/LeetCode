#
# @lc app=leetcode.cn id=696 lang=python3
#
# [696] 计数二进制子串
#

# Accepted
# 90/90 cases passed (192 ms)
# Your runtime beats 66.67 % of python3 submissions
# Your memory usage beats 14.29 % of python3 submissions (14 MB)

# @lc code=start
class Solution(object):
    def countBinarySubstrings(self, s):
        ans, prev, cur = 0, 0, 1
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                ans += min(prev, cur)
                prev, cur = cur, 1
            else:
                cur += 1

        return ans + min(prev, cur)

        
# @lc code=end

