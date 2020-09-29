#
# @lc app=leetcode.cn id=859 lang=python3
#
# [859] 亲密字符串
#
# Accepted
# 29/29 cases passed (40 ms)
# Your runtime beats 85.39 % of python3 submissions
# Your memory usage beats 5.05 % of python3 submissions (13.7 MB)
# @lc code=start
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        diff_index_0 = -1
        diff_index_1 = -1
        if A == B:
            seen = set()
            for a in A:
                if a in seen:
                    return True
                seen.add(a)
            return False
        for index, each in enumerate(A):
            if each not in B:
                return False
            if each != B[index]:
                if diff_index_0 == -1:
                    diff_index_0 = index
                    continue
                elif diff_index_1 == -1:
                    diff_index_1 = index
                    break
                else:
                    pass
        A = list(A)
        B = list(B)
        temp = A[diff_index_0]
        A[diff_index_0] = A[diff_index_1]
        A[diff_index_1] = temp
        return A == B
# @lc code=end

