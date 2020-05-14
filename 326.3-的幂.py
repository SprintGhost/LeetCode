#
# @lc app=leetcode.cn id=326 lang=python3
#
# [326] 3的幂
#

# Accepted
# 21038/21038 cases passed (100 ms)
# Your runtime beats 46.61 % of python3 submissions
# Your memory usage beats 5.29 % of python3 submissions (13.7 MB)
# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        while(n % 3 == 0):
            n = n // 3
        return n == 1
# @lc code=end

