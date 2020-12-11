#
# @lc app=leetcode.cn id=985 lang=python3
#
# [985] 查询后的偶数和
#
# Accepted
# 58/58 cases passed (552 ms)
# Your runtime beats 98.24 % of python3 submissions
# Your memory usage beats 48.32 % of python3 submissions (19.5 MB)
# @lc code=start
class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        result = list()
        pre_A = 0
        for each_a in A:
            if each_a % 2 == 0:
                pre_A += each_a
        for each in queries:
            if A[each[1]] % 2 == 0:
                if (A[each[1]] + each[0]) % 2 == 0:
                    pre_A += each[0]
                else:
                    pre_A -= A[each[1]]
            else:
                if (A[each[1]] + each[0]) % 2 == 0:
                    pre_A += each[0] + A[each[1]]
                else:
                    pass
            result.append(pre_A)
            A[each[1]] += each[0]

        return result


        
# @lc code=end

