#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        brackets_dict = {
            "(":")",
            "[":"]",
            "{":"}",
        }
        if (len(s) == 0):
            return True
        if (len(s) % 2 != 0):
            return False
        store_brackets = list()
        index = 0
        for brackets in s:
            if brackets in brackets_dict:
                store_brackets.append(brackets)
                index = index + 1
            else:
                if len(store_brackets) == 0:
                    return False
                if brackets_dict[store_brackets[index - 1]] == brackets:
                    store_brackets.pop(index - 1)
                    index = index - 1
                else:
                    return False

        if len(store_brackets) != 0:
            return False
        else:
            return True 

# A = Solution()
# print (A.isValid("){"))
        
# @lc code=end

