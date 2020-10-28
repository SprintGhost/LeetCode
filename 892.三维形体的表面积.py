#
# @lc app=leetcode.cn id=892 lang=python3
#
# [892] 三维形体的表面积
#
# Accepted
# 90/90 cases passed (136 ms)
# Your runtime beats 35.7 % of python3 submissions
# Your memory usage beats 56.17 % of python3 submissions (13.4 MB)
# @lc code=start
class Solution(object):
    def surfaceArea(self, grid):
        N = len(grid)

        ans = 0
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    ans += 2
                    for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r,c+1)):
                        if 0 <= nr < N and 0 <= nc < N:
                            nval = grid[nr][nc]
                        else:
                            nval = 0

                        ans += max(grid[r][c] - nval, 0)

        return ans

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/surface-area-of-3d-shapes/solution/san-wei-xing-ti-de-biao-mian-ji-by-leetcode-soluti/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        
        
# @lc code=end

