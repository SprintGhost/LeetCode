#
# @lc app=leetcode.cn id=686 lang=python3
#
# [686] 重复叠加字符串匹配
#

# Accepted
# 55/55 cases passed (152 ms)
# Your runtime beats 33.9 % of python3 submissions
# Your memory usage beats 20 % of python3 submissions (13.7 MB)

# @lc code=start
class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        if B in A:
            return 1
        num = 1
        a = A
        while True:
            num += 1
            A += a
            if B in A:
                return num
            if len(A)>len(B)+len(a):
                return -1

        
        
# @lc code=end

