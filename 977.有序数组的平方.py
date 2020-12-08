#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#
# Accepted
# 137/137 cases passed (84 ms)
# Your runtime beats 99.25 % of python3 submissions
# Your memory usage beats 99.8 % of python3 submissions (14.6 MB)

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for index, each in enumerate(nums):
            nums[index] = each ** 2
        return sorted(nums)

# Accepted
# 137/137 cases passed (92 ms)
# Your runtime beats 99.16 % of python3 submissions
# Your memory usage beats 95.26 % of python3 submissions (14.9 MB)
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        n = len(A)
        ans = [0] * n
        
        i, j, pos = 0, n - 1, n - 1
        while i <= j:
            if A[i] * A[i] > A[j] * A[j]:
                ans[pos] = A[i] * A[i]
                i += 1
            else:
                ans[pos] = A[j] * A[j]
                j -= 1
            pos -= 1
        
        return ans

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/squares-of-a-sorted-array/solution/you-xu-shu-zu-de-ping-fang-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# @lc code=end

