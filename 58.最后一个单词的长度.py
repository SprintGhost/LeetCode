#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# Accepted
# 59/59 cases passed (32 ms)
# Your runtime beats 86.75 % of python3 submissions
# Your memory usage beats 99.66 % of python3 submissions (12.6 MB)

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0
        # Use split function, of course we can use a function replace it
        s_split = s.split(" ")
        index = len(s_split) - 1
        while(index >= 0):
            if "" != s_split[index]:
                return len(s_split[index])
            index -= 1
        return 0


# 59/59 cases passed (36 ms)
# Your runtime beats 73.11 % of python3 submissions
# Your memory usage beats 99.41 % of python3 submissions (12.9 MB)


# Another solution replace split function

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0
        index = len(s)
        last_word_flag = False
        last_word_len = 0
        while(index > 0):
            index -= 1
            if " " == s[index] and last_word_flag:
                break
            if " " == s[index]:
                continue
            if (not last_word_flag):
                last_word_flag = True
            last_word_len += 1
        return last_word_len


# Accepted
# 59/59 cases passed (32 ms)
# Your runtime beats 86.75 % of python3 submissions
# Your memory usage beats 99.66 % of python3 submissions (12.6 MB)
# Solution from leetcode

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        end = len(s) - 1
        while(end >= 0 and s[end] == ' '):
            end -= 1
        if(end < 0):
             return 0
        start = end
        while(start >= 0 and s[start] != ' '):
            start -= 1
        return end - start


# A = Solution()
# print (A.lengthOfLastWord("a      "))
# @lc code=end

