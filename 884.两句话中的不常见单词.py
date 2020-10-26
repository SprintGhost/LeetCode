#
# @lc app=leetcode.cn id=884 lang=python3
#
# [884] 两句话中的不常见单词
#
# Accepted
# 53/53 cases passed (44 ms)
# Your runtime beats 52.06 % of python3 submissions
# Your memory usage beats 69.94 % of python3 submissions (13.3 MB)
# @lc code=start
class Solution:
    def uncommonFromSentences(self, A: str, B: str):
        result = list()
        A = A.split(" ")
        B = B.split(" ")
        temp = dict()
        for index, each in enumerate(A):
            if (each not in B) and (each not in A[index + 1:]) and (each not in temp):
                result.append(each)
            temp[each] = 0
        temp = dict()
        for index, each in enumerate(B):
            if (each not in A) and (each not in B[index + 1:]) and (each not in temp):
                result.append(each)
            temp[each] = 0
        return result

# A = Solution()
# A.uncommonFromSentences("apple apple","banana")
# @lc code=end

