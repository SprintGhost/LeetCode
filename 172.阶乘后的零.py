#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#

# Accepted
# 502/502 cases passed (28 ms)
# Your runtime beats 92.1 % of python3 submissions
# Your memory usage beats 51.39 % of python3 submissions (13 MB)

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 0
        while(n > 0):
            result += n // 5
            n = n // 5
        return result


# def test(n):
#     if n == 1:
#         return 1
#     else:
#         return n * test(n - 1)
# print(test(100))
# A = Solution()
# print(A.trailingZeroes(25))
# @lc code=end

