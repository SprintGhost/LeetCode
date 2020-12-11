#
# @lc app=leetcode.cn id=905 lang=python3
#
# [905] 按奇偶排序数组
#

# Accepted
# 285/285 cases passed (100 ms)
# Your runtime beats 59.29 % of python3 submissions
# Your memory usage beats 5.06 % of python3 submissions (14.2 MB)
# @lc code=start
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        result = list()
        zero_number = [0] * len(A)
        start = 0
        end = len(A) - 1
        for each in A:
            if each % 2 == 0:
                result.insert(start,each)
                if each == 0:
                    start += 1
            else:
                result.insert(end, each)
        return result

# Accepted
# 285/285 cases passed (96 ms)
# Your runtime beats 76.02 % of python3 submissions
# Your memory usage beats 11.03 % of python3 submissions (14.1 MB)
class Solution(object):
    def sortArrayByParity(self, A):
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] % 2 > A[j] % 2:
                A[i], A[j] = A[j], A[i]

            if A[i] % 2 == 0: i += 1
            if A[j] % 2 == 1: j -= 1

        return A

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/sort-array-by-parity/solution/an-qi-ou-pai-xu-shu-zu-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# @lc code=end

