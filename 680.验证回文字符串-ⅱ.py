#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#


# Accepted
# 460/460 cases passed (196 ms)
# Your runtime beats 36.29 % of python3 submissions
# Your memory usage beats 36.36 % of python3 submissions (14.1 MB)
# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        index_start = 0
        index_end = len(s) - 1
        del_flag_left = False
        del_flag_right = False
        pre_start = index_start
        pre_end = index_end
        while index_start <= index_end:
            if (s[index_end] != s[index_start]):
                if del_flag_left or del_flag_right:
                    index_start = pre_start
                    index_end = pre_end
                if del_flag_right and del_flag_right:
                    return False
                if ((index_start + 1) == index_end):
                    return True
                elif not del_flag_left and (s[index_end - 1] == s[index_start]):
                    del_flag_left = True
                    pre_end = index_end
                    pre_start = index_start
                    index_start += 1
                    index_end -= 2
                    continue
                elif not del_flag_right and (s[index_end] == s[index_start + 1]):
                    del_flag_right = True
                    pre_end = index_end
                    pre_start = index_start
                    index_start += 2
                    index_end -= 1
                    continue
                else:
                    return False         
            else:
                index_end -= 1
                index_start += 1
        return True

# The following solution is more concise
# Accepted
# 460/460 cases passed (244 ms)
# Your runtime beats 14.27 % of python3 submissions
# Your memory usage beats 36.36 % of python3 submissions (14.1 MB)

class Solution:
    def palindrome(self,s, i, j):
        while (i < j and (s[i] == s[j])):
            i += 1
            j -= 1
            pass
        return i >= j
    
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while (i < j and (s[i] == s[j])):
            i += 1
            j -= 1
            pass      
        return self.palindrome(s, i, j - 1) or self.palindrome(s, i + 1, j)

# A = Solution()
# A.validPalindrome("ebcbbececabbacecbbcbe") 
# @lc code=end

