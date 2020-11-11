#
# @lc app=leetcode.cn id=908 lang=python3
#
# [908] 最小差值 I
#
# Accepted
# 68/68 cases passed (128 ms)
# Your runtime beats 99.08 % of python3 submissions
# Your memory usage beats 5.24 % of python3 submissions (14.9 MB)
# @lc code=start
class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        # A = sorted(A)
        # min_max_differ = (A[len(A) - 1] - A[0])
        #  use sorted funtion will cost lots of time
        min_max_differ = max(A) - min(A)
        K = 2 * K
        if min_max_differ > K:
            return min_max_differ - K
        else:
            return 0
        
# @lc code=end

