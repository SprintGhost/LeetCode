#
# @lc app=leetcode.cn id=914 lang=python3
#
# [914] 卡牌分组
#
# Accepted
# 74/74 cases passed (44 ms)
# Your runtime beats 89.79 % of python3 submissions
# Your memory usage beats 19.41 % of python3 submissions (13.7 MB)
# @lc code=start
class Solution:
    def hasGroupsSizeX(self, deck) -> bool:
        from math import gcd
        from collections import Counter
        from functools import reduce
        vals = Counter(deck).values()
        return reduce(gcd, vals) >= 2
  
# @lc code=end

