#
# @lc app=leetcode.cn id=299 lang=python3
#
# [299] 猜数字游戏
#

# Accepted
# 152/152 cases passed (72 ms)
# Your runtime beats 23.57 % of python3 submissions
# Your memory usage beats 5.88 % of python3 submissions (13.6 MB)

# @lc code=start
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        Bulls = 0
        Cows = 0
        temp = dict()
        for each in secret:
            if each in temp:
                temp[each] += 1
            else:
                temp[each] = 1
        for index, each in enumerate(guess):
                if guess[index] == secret[index]:
                    Bulls += 1
                    temp[each] -= 1
        for index, each in enumerate(guess):
                if (guess[index] != secret[index]) and (each in temp) and (temp[each] > 0):
                    Cows += 1
                    temp[each] -= 1
        return str(Bulls) + "A" + str(Cows) + "B"

# A = Solution()
# print(A.getHint("1122", "1222"))

# @lc code=end

