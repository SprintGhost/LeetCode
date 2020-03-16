#
# @lc app=leetcode.cn id=278 lang=python3
#
# [278] 第一个错误的版本
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
#     if version > 1:
#         return True

# Accepted
# 22/22 cases passed (48 ms)
# Your runtime beats 14.04 % of python3 submissions
# Your memory usage beats 5.11 % of python3 submissions (13.5 MB)

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        right = n
        left = 1
        while right > left:
            mid =  (right + left) >> 1
            if isBadVersion(mid):
                right = mid
            else: 
                left = mid + 1
        return left


# @lc code=end

