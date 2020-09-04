#
# @lc app=leetcode.cn id=796 lang=python3
#
# [796] 旋转字符串
#
# Accepted
# 45/45 cases passed (32 ms)
# Your runtime beats 95.76 % of python3 submissions
# Your memory usage beats 21.05 % of python3 submissions (13.7 MB)
# @lc code=start
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if A == B:
            return True
        b_start = B[0]
        temp = list(A)
        temp_index_list = list()
        index = 0
        if b_start not in A:
            return False
        while b_start in temp:
            temp_index_list.append(temp.index(b_start) + index)
            temp.pop(temp.index(b_start))
            index += 1
        for each in temp_index_list:
            if A[each:]+A[:each] == B:
                return True
        return False
        
# A = Solution()
# A.rotateString("bbbacddceeb","ceebbbbacdd")
# @lc code=end

