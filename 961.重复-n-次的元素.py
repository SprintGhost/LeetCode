#
# @lc app=leetcode.cn id=961 lang=python3
#
# [961] 重复 N 次的元素
#
# Accepted
# 102/102 cases passed (44 ms)
# Your runtime beats 93.97 % of python3 submissions
# Your memory usage beats 18.74 % of python3 submissions (14.6 MB)
# @lc code=start
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        for k in range(1, 4):
            for i in range(len(A) - k):
                if A[i] == A[i+k]:
                    return A[i]

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/n-repeated-element-in-size-2n-array/solution/zhong-fu-n-ci-de-yuan-su-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# @lc code=end

