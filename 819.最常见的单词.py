#
# @lc app=leetcode.cn id=819 lang=python3
#
# [819] 最常见的单词
#
# Accepted
# 47/47 cases passed (52 ms)
# Your runtime beats 34.53 % of python3 submissions
# Your memory usage beats 46.13 % of python3 submissions (13.7 MB)
# @lc code=start
class Solution:
    def mostCommonWord(self, paragraph, banned) -> str:
        paragraph = paragraph.lower()
        temp = dict()
        word = str()
        for each in paragraph:
            if each.isalpha():
                word += each
            else:
                if word != "" and word not in banned:
                    if word not in temp:
                        temp[word] = 1
                    else:
                        temp[word] += 1
                word = str()
        if word != "" and word not in banned:
            if word not in temp:
                temp[word] = 1
            else:
                temp[word] += 1
        return max(zip(temp.values(),temp.keys()))[1]
# Accepted
# 47/47 cases passed (44 ms)
# Your runtime beats 77.55 % of python3 submissions
# Your memory usage beats 52.8 % of python3 submissions (13.7 MB)
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        banset = set(banned)
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        count = collections.Counter(
            word for word in paragraph.lower().split())

        ans, best = '', 0
        for word in count:
            if count[word] > best and word not in banset:
                ans, best = word, count[word]

        return ans

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/most-common-word/solution/zui-chang-jian-de-dan-ci-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# A = Solution()
# A.mostCommonWord("Bob. hIt, baLl",["bob", "hit"])    
# @lc code=end

