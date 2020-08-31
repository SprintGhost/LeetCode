#
# @lc app=leetcode.cn id=766 lang=python3
#
# [766] 托普利茨矩阵
#
# Accepted
# 482/482 cases passed (128 ms)
# Your runtime beats 17.9 % of python3 submissions
# Your memory usage beats 12.77 % of python3 submissions (13.8 MB)
# @lc code=start
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        groups = {}
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r-c not in groups:
                    groups[r-c] = val
                elif groups[r-c] != val:
                    return False
        return True

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/toeplitz-matrix/solution/tuo-pu-li-ci-ju-zhen-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# Accepted
# 482/482 cases passed (140 ms)
# Your runtime beats 9.15 % of python3 submissions
# Your memory usage beats 86.13 % of python3 submissions (13.6 MB)
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        return all(r == 0 or c == 0 or matrix[r-1][c-1] == val
                   for r, row in enumerate(matrix)
                   for c, val in enumerate(row))

           

        
# @lc code=end

