#
# @lc app=leetcode.cn id=720 lang=python3
#
# [720] 词典中最长的单词
#

# @lc code=start
# class Solution:
#     def longestWord(self, words: List[str]) -> str:
#         result = None
#         max_index = 0xfffffff
#         for index, each in enumerate(words):
#             if len(each) == 1:
#                 continue
#             if (each[:-1] in words):
#                 if result == None: #or (len(result) == len(each) and max_index > index):
#                     result = each
#                 elif len(result) < len(each):
#                     result = each
#                 else:
#                     pass
                
#         return result

from collections import *

class Solution(object):
    def longestWord(self, words):
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        END = True

        for i, word in enumerate(words):
            reduce(dict.__getitem__, word, trie)[END] = i

        stack = trie.values()
        ans = ""
        while stack:
            cur = stack.pop()
            if END in cur:
                word = words[cur[END]]
                if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                    ans = word
                stack.extend([cur[letter] for letter in cur if letter != END])

        return ans

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/longest-word-in-dictionary/solution/ci-dian-zhong-zui-chang-de-dan-ci-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# @lc code=end

