#
# @lc app=leetcode.cn id=840 lang=python3
#
# [840] 矩阵中的幻方
#
# Accepted
# 91/91 cases passed (44 ms)
# Your runtime beats 86.34 % of python3 submissions
# Your memory usage beats 19.58 % of python3 submissions (13.5 MB)
# @lc code=start
class Solution(object):
    def numMagicSquaresInside(self, grid):
        R, C = len(grid), len(grid[0])

        def magic(a,b,c,d,e,f,g,h,i):
            return (sorted([a,b,c,d,e,f,g,h,i]) == list(range(1, 10)) and
                (a+b+c == d+e+f == g+h+i == a+d+g == b+e+h == c+f+i == a+e+i == c+e+g == 15))

        ans = 0
        for r in range(R-2):
            for c in range(C-2):
                if grid[r+1][c+1] != 5: continue  # optional skip
                if magic(grid[r][c], grid[r][c+1], grid[r][c+2],
                         grid[r+1][c], grid[r+1][c+1], grid[r+1][c+2],
                         grid[r+2][c], grid[r+2][c+1], grid[r+2][c+2]):
                    ans += 1
        return ans

# @lc code=end

