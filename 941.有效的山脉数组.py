#
# @lc app=leetcode.cn id=941 lang=python3
#
# [941] 有效的山脉数组
#
# Accepted
# 52/52 cases passed (48 ms)
# Your runtime beats 99.92 % of python3 submissions
# Your memory usage beats 97.19 % of python3 submissions (14.4 MB)
# @lc code=start
class Solution:
    def validMountainArray(self, arr) -> bool:
        arr_len = len(arr)
        start_reverse = False
        before = arr[0]
        if arr_len < 3:
            return False
        for index in range(1,arr_len):
            if start_reverse:
                if  (before <= arr[index]):
                    return False
                else:
                    before = arr[index] 
            elif not start_reverse:
                if (before > arr[index]):
                    if index == 1:
                        return False
                    start_reverse = True
                    before = arr[index]
                elif before == arr[index]:
                    return False
                else:
                    before = arr[index]
        return start_reverse


# Accepted
# 52/52 cases passed (68 ms)
# Your runtime beats 97.67 % of python3 submissions
# Your memory usage beats 99 % of python3 submissions (14.3 MB)
# Other solution from leetcode
class Solution(object):
    def validMountainArray(self, A):
        N = len(A)
        i = 0
        while i + 1 < N and A[i] < A[i + 1]:
            i += 1
        if i == 0 or i == N - 1:
            return False
        while i + 1 < N and A[i] > A[i + 1]:
            i += 1

        return i == N - 1


                    
# A = Solution()
# A.validMountainArray([3,2,1])

# @lc code=end

