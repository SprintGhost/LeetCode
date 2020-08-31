#
# @lc app=leetcode.cn id=744 lang=python3
#
# [744] 寻找比目标字母大的最小字母
#
# Accepted
# 165/165 cases passed (144 ms)
# Your runtime beats 37.63 % of python3 submissions
# Your memory usage beats 46.25 % of python3 submissions (14 MB)
# Brute force search
# Accepted
# 165/165 cases passed (128 ms)
# Your runtime beats 95.13 % of python3 submissions
# Your memory usage beats 80.46 % of python3 submissions (13.9 MB)
# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target == 'z':
            return letters[0]
        for each in letters:
            if each > target:
                return each
        return letters[0]
# @lc code=end

