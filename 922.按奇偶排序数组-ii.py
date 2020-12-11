#
# @lc app=leetcode.cn id=922 lang=python3
#
# [922] 按奇偶排序数组 II
#

# Accepted
# 61/61 cases passed (220 ms)
# Your runtime beats 94.62 % of python3 submissions
# Your memory usage beats 37.91 % of python3 submissions (15.8 MB)

# @lc code=start
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        result = [0] * len(A)
        odd_index = 1
        even_index = 0
        for each in A:
            if each % 2 == 0:
                result[even_index] = each
                even_index += 2
            else:
                result[odd_index] = each
                odd_index += 2
        return result

# Accepted
# 61/61 cases passed (232 ms)
# Your runtime beats 75.2 % of python3 submissions
# Your memory usage beats 86.27 % of python3 submissions (15.6 MB)
        a_len = len(A)
        index_i = 0
        index_j = 1
        for index_i in range(0,a_len, 2):
            if A[index_i] % 2 == 1:
                while (A[index_j] % 2 == 1):
                    index_j += 2
                temp = A[index_i]
                A[index_i] = A[index_j]
                A[index_j] = temp
        return A
# @lc code=end

