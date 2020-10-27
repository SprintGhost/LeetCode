#
# @lc app=leetcode.cn id=888 lang=python3
#
# [888] 公平的糖果交换
#

# Accepted
# 75/75 cases passed (3416 ms)
# Your runtime beats 40.34 % of python3 submissions
# Your memory usage beats 62.58 % of python3 submissions (15.3 MB)

# @lc code=start
class Solution:
    def fairCandySwap(self, A, B):
        sum_a = sum(A)
        sum_b = sum(B)
        temp = abs((sum_a - sum_b)) // 2
        if sum_a < sum_b:
            for each in A:
                if (each + temp) in B:
                    return [each, each+temp]
        else:
            for each in B:
                if (each + temp) in A:
                    return[each + temp, each]
        return None

# Accepted
# 75/75 cases passed (504 ms)
# Your runtime beats 62.33 % of python3 submissions
# Your memory usage beats 13.75 % of python3 submissions (15.8 MB)

class Solution(object):
    def fairCandySwap(self, A, B):
        Sa, Sb = sum(A), sum(B)
        setB = set(B)
        for x in A:
            if x + (Sb - Sa) / 2 in setB:
                return [x, x + (Sb - Sa) / 2]

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/fair-candy-swap/solution/gong-ping-de-tang-guo-jiao-huan-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# A = Solution()
# A.fairCandySwap([1,1],[2,2])
# @lc code=end

