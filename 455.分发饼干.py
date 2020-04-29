#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# Accepted
# 21/21 cases passed (208 ms)
# Your runtime beats 59.26 % of python3 submissions
# Your memory usage beats 50 % of python3 submissions (15.4 MB)

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        index_g = 0
        index_s = 0
        while (index_g < len(g)) and (index_s < len(s)):
            if g[index_g] <= s[index_s]:
                index_s += 1
                index_g += 1
            else:
                index_s += 1
        return index_g
# @lc code=end

