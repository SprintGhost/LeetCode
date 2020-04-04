#
# @lc app=leetcode.cn id=374 lang=python3
#
# [374] 猜数字大小
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:


# Accepted
# 25/25 cases passed (40 ms)
# Your runtime beats 41.09 % of python3 submissions
# Your memory usage beats 5.95 % of python3 submissions (13.6 MB)

class Solution:
    def guessNumber(self, n: int) -> int:
        if n == 1:
            return 1
        left = 0
        mid = n // 2
        right = n
        while left < right:
            if guess(mid) == 0:
                return mid
            elif guess(mid) == 1:
                left = mid
                mid = (left + right) // 2 + 1
            else:
                right = mid
                mid = (left + right) // 2
        return mid
        
# @lc code=end

