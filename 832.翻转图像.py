#
# @lc app=leetcode.cn id=832 lang=python3
#
# [832] 翻转图像
#
# Accepted
# 82/82 cases passed (68 ms)
# Your runtime beats 51.16 % of python3 submissions
# Your memory usage beats 57.91 % of python3 submissions (13.3 MB)
# @lc code=start
class Solution:
    def flipAndInvertImage(self, A):
        for index_i in range(len(A)):
            for index_j in range(len(A[index_i])):
                if A[index_i][index_j] == 0:
                    A[index_i][index_j] = 1
                else:
                    A[index_i][index_j] = 0
            A[index_i] = A[index_i][::-1]
        return A

# A = Solution()
# A.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]])
# @lc code=end

