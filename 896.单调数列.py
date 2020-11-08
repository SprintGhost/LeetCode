#
# @lc app=leetcode.cn id=896 lang=python3
#
# [896] 单调数列
#

# Accepted
# 366/366 cases passed (536 ms)
# Your runtime beats 94.71 % of python3 submissions
# Your memory usage beats 5.08 % of python3 submissions (19.9 MB)
# @lc code=start
class Solution:
    def isMonotonic(self, A) -> bool:
        temp = sorted(A)
        if temp == A:
            return True
        temp = sorted(A,reverse=True)
        if temp == A:
            return True
        return False


# Another solution
# Accepted
# 366/366 cases passed (540 ms)
# Your runtime beats 93.91 % of python3 submissions
# Your memory usage beats 10.98 % of python3 submissions (19.6 MB)
class Solution(object):
    def isMonotonic(self, A):
        i = 0
        j = 0
        for k in range(len(A) - 1):
            if(A[k]<A[k+1]):
                    i += 1
            elif(A[k]>A[k+1]):
                    j += 1
            if(i!=0 and j!=0):
                return False
        return i*j==0

# A = Solution()
# A.isMonotonic([6,5,4,4])
# @lc code=end

