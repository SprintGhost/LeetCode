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
# class Solution:
#     def uncommonFromSentences(self, A: str, B: str):
#         result = list()
#         A = A.split(" ")
#         B = B.split(" ")
#         temp = dict()
#         for index, each in enumerate(A):
#             if (each not in B) and (each not in A[index + 1:]) and (each not in temp):
#                 result.append(each)
#             temp[each] = 0
#         temp = dict()
#         for index, each in enumerate(B):
#             if (each not in A) and (each not in B[index + 1:]) and (each not in temp):
#                 result.append(each)
#             temp[each] = 0
#         return result

# Accepted
# 53/53 cases passed (32 ms)
# Your runtime beats 97.32 % of python3 submissions
# Your memory usage beats 5.41 % of python3 submissions (13.6 MB)
# The following solution is best
class Solution(object):
    def uncommonFromSentences(self, A, B):
        count = {}
        for word in A.split():
            count[word] = count.get(word, 0) + 1
        for word in B.split():
            count[word] = count.get(word, 0) + 1

        #Alternatively:
        #count = collections.Counter(A.split())
        #count += collections.Counter(B.split())

        return [word for word in count if count[word] == 1]

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/uncommon-words-from-two-sentences/solution/liang-ju-hua-zhong-de-bu-chang-jian-dan-ci-by-leet/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# A = Solution()
# A.uncommonFromSentences("apple apple","banana")
# @lc code=end

