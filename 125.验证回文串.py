#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# Accepted
# 476/476 cases passed (84 ms)
# Your runtime beats 15.97 % of python3 submissions
# Your memory usage beats 74.24 % of python3 submissions (13.6 MB)

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        index_start = 0
        index_end = len(s)- 1
        while(index_end > index_start):
            if not s[index_start].isalnum():
                index_start += 1
                continue
            if not s[index_end].isalnum():
                index_end -= 1
                continue
            if s[index_end].lower() != s[index_start].lower():
                return False
            index_start += 1
            index_end -= 1
        return True

# A = Solution()
# A.isPalindrome("A man, a plan, a canal: Panama")


# Attention: 
# The following method is simple
# but it is important to note that
# the filter function in Python is not clear
# if there are any alternative functions in other languages

# Accepted
# 476/476 cases passed (36 ms)
# Your runtime beats 97.79 % of python3 submissions
# Your memory usage beats 36.53 % of python3 submissions (14.4 MB)


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [*filter(str.isalnum, s.lower())]
        return s == s[::-1]

# 作者：QQqun902025048
# 链接：https://leetcode-cn.com/problems/valid-palindrome/solution/c-5xing-on-by-qqqun902025048-2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# @lc code=end

