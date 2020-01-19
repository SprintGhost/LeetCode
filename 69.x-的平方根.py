#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#


# @lc code=start
# Accepted
# 1017/1017 cases passed (40 ms)
# Your runtime beats 84.24 % of python3 submissions
# Your memory usage beats 31.03 % of python3 submissions (13.3 MB)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left = 0
        right = x // 2 + 1
        while (left < right):
            mid = (left + right + 1) >> 1
            square = mid * mid
            if square > x:
                right = mid - 1
            else:
                left = mid
        return left


# Accepted
# 1017/1017 cases passed (40 ms)
# Your runtime beats 84.24 % of python3 submissions
# Your memory usage beats 53.88 % of python3 submissions (13.2 MB)

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        cur = 1
        while True:
            pre = cur
            cur = (cur + x/cur) / 2
            if abs(cur - pre) < 1e-6:
                return int(cur)

# @lc code=end

