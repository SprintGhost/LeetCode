#
# @lc app=leetcode.cn id=598 lang=python3
#
# [598] 范围求和 II
#

# Accepted
# 69/69 cases passed (100 ms)
# Your runtime beats 31.72 % of python3 submissions
# Your memory usage beats 33.33 % of python3 submissions (15.6 MB)

# @lc code=start
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_j = 0xffffffff
        min_i = 0xffffffff
        if not ops:
            return m * n
        for each in ops:
            if each[0] <= m:
                min_i = min(each[0], min_i)
            else:
                min_i = min(min_i, m)
            if each[1] <= n:
                min_j = min(each[1], min_j)
            else:
                min_j = min(min_j, n)
        return min_i * min_j
            

# @lc code=end

