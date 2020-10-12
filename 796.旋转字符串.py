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
# Accepted
# 45/45 cases passed (36 ms)
# Your runtime beats 85.57 % of python3 submissions
# Your memory usage beats 42.11 % of python3 submissions (13.7 MB)
class Solution(object):
    def rotateString(self, A, B):
        return len(A) == len(B) and B in A+A

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/rotate-string/solution/xuan-zhuan-zi-fu-chuan-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# A = Solution()
# A.rotateString("bbbacddceeb","ceebbbbacdd")
# @lc code=end

