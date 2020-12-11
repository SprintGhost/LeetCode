#
# @lc app=leetcode.cn id=970 lang=python3
#
# [970] 强整数
#

# Accepted
# 93/93 cases passed (72 ms)
# Your runtime beats 13.98 % of python3 submissions
# Your memory usage beats 18.7 % of python3 submissions (13.5 MB)

# @lc code=start
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        result = set()
        for i in range(20):
            for j in range(20):
                v = x ** i + y ** j
                if v <= bound:
                    result.add(v)
        return list(result)

        
# @lc code=end

