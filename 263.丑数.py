#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] 丑数
#

# Accepted
# 1012/1012 cases passed (40 ms)
# Your runtime beats 45.25 % of python3 submissions
# Your memory usage beats 5.18 % of python3 submissions (13.6 MB)

# @lc code=start
class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 0:
            return False
        while (num > 1) or (num <= -1):
            if (num % 2 == 0):
                num = num // 2
                continue
            if (num % 3 == 0):
                num = num // 3
                continue
            if (num % 5 == 0):
                num = num // 5
                continue
            return False
        return True
    
# A = Solution()
# print(A.isUgly(-2147483648))
# @lc code=end

