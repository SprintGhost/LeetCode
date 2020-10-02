#
# @lc app=leetcode.cn id=867 lang=python3
#
# [867] 转置矩阵
#
# Accepted
# 36/36 cases passed (92 ms)
# Your runtime beats 69.68 % of python3 submissions
# Your memory usage beats 7.1 % of python3 submissions (14.2 MB)
# @lc code=start
class Solution(object):
    def transpose(self, A):
        R, C = len(A), len(A[0])
        ans = [[None] * R for _ in range(C)]
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                ans[c][r] = val
        return ans

        #Alternative Solution:
        #return zip(*A)

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/transpose-matrix/solution/zhuan-zhi-ju-zhen-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        
# @lc code=end

