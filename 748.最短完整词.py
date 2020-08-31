#
# @lc app=leetcode.cn id=748 lang=python3
#
# [748] 最短完整词
#

# Accepted
# 102/102 cases passed (96 ms)
# Your runtime beats 45.48 % of python3 submissions
# Your memory usage beats 86.36 % of python3 submissions (13.7 MB)

# @lc code=start
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        def count(itera):
            ans = [0] * 26
            for letter in itera:
                ans[ord(letter) - ord('a')] += 1
            return ans

        def dominates(c1, c2):
            return all(x1 >= x2 for x1, x2 in zip(c1, c2))

        ans = None
        target = count(c.lower() for c in licensePlate if c.isalpha())
        for word in words:
            if ((ans is None or (len(word) < len(ans))) and
                    dominates(count(word.lower()), target)):
                ans = word

        return ans

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/shortest-completing-word/solution/zui-duan-wan-zheng-ci-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# form collections import Counter
# def shortestCompletingWord(licensePlate, words)：
#       words = sorted(words,key = lambda x: len(x))
#       tmp_str =  ''.join(item.lower() for item in licensePlate if item.isalpha())
#       str_dict =dict( Counter(tmp_str))

#        for word in words:
#             word_dict = dict(Counter(word))
#             for letter, value in str_dict .items():
#                 if letter not in word_dict or value > word_dict[letter] :
#                    break
#             else:
#                   return word



# @lc code=end

