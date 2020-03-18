#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#

# Accepted
# 33/33 cases passed (24 ms)
# Your runtime beats 96.68 % of python3 submissions
# Your memory usage beats 5.11 % of python3 submissions (13.5 MB)

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split(" ")
        # Map solution;
        # Accepted
        # 33/33 cases passed (36 ms)
        # Your runtime beats 52.72 % of python3 submissions
        # Your memory usage beats 5.11 % of python3 submissions (13.5 MB)
        return list(map(pattern.index, pattern))==list(map(words.index,words))
        if len(words) != len(pattern):
            return False
        temp = dict()
        for index, each in enumerate(pattern):
            if each in temp:
                if temp[each] != words[index]:
                    return False
            else:
                for each_1 in temp:
                    if temp[each_1] == words[index]:
                        return False
                temp[each] = words[index]
        return True


# A = Solution()
# print(A.wordPattern("abba", "dog dog dog dog"))
# @lc code=end

