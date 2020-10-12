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
# Following solution is fanster than my solution
# Accepted
# 82/82 cases passed (60 ms)
# Your runtime beats 88.5 % of python3 submissions
# Your memory usage beats 46.82 % of python3 submissions (13.4 MB)
class Solution(object):
    def flipAndInvertImage(self, A):
        for row in A:
            for i in range((len(row) + 1) // 2):
                """
                In Python, the shortcut row[~i] = row[-i-1] = row[len(row) - 1 - i]
                helps us find the i-th value of the row, counting from the right.
                """
                row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
        return A

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/flipping-an-image/solution/fan-zhuan-tu-xiang-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# A = Solution()
# A.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]])
# @lc code=end

