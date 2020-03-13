#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#

# Accepted
# 1108/1108 cases passed (40 ms)
# Your runtime beats 44.5 % of python3 submissions
# Your memory usage beats 28.03 % of python3 submissions (13.5 MB)

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        while n != 0:
            temp = n >> 1
            if (temp != 0) and ((n & 1) != 0):
                return False
            n = temp
        return True



class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False

        # Accepted
        # 1108/1108 cases passed (40 ms)
        # Your runtime beats 44.5 % of python3 submissions
        # Your memory usage beats 28.03 % of python3 submissions (13.5 MB)
        return n & (-n) == n

        # Accepted
        # 1108/1108 cases passed (40 ms)
        # Your runtime beats 44.5 % of python3 submissions
        # Your memory usage beats 28.03 % of python3 submissions (13.2 MB)
        return n & (n - 1) == 0

# @lc code=end

