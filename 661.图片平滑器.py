#
# @lc app=leetcode.cn id=661 lang=python3
#
# [661] 图片平滑器
#

# Accepted
# 202/202 cases passed (872 ms)
# Your runtime beats 48.01 % of python3 submissions
# Your memory usage beats 33.33 % of python3 submissions (14.4 MB)

import math
# @lc code=start
class Solution(object):
    def imageSmoother(self, M):
        R, C = len(M), len(M[0])
        ans = [[0] * C for _ in M]

        for r in range(R):
            for c in range(C):
                count = 0
                for nr in (r-1, r, r+1):
                    for nc in (c-1, c, c+1):
                        if 0 <= nr < R and 0 <= nc < C:
                            ans[r][c] += M[nr][nc]
                            count += 1
                ans[r][c] = math.floor(ans[r][c]/count)

        return ans

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/image-smoother/solution/tu-pian-ping-hua-qi-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        
        
# @lc code=end

