#
# @lc app=leetcode.cn id=976 lang=python3
#
# [976] 三角形的最大周长
#
# Accepted
# 84/84 cases passed (208 ms)
# Your runtime beats 97.95 % of python3 submissions
# Your memory usage beats 39.31 % of python3 submissions (14.8 MB)
# @lc code=start
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        a = 0
        b = 0
        c = 0
        A = sorted(A,reverse=True)
        index = 2
        while index  < len(A):
            a = A[index - 2]
            b = A[index - 1]
            c = A[index]
            if c + b > a:
                return a + b + c
            index += 1
        return 0


        
# @lc code=end

