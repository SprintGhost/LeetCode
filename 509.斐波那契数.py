#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# Accepted
# 31/31 cases passed (900 ms)
# Your runtime beats 13.54 % of python3 submissions
# Your memory usage beats 5.55 % of python3 submissions (13.7 MB)

# @lc code=start
# class Solution:
#     def fib(self, N: int) -> int:
#         if N == 0:
#             return 0
#         if N == 1:
#             return 1
#         return self.fib(N - 1) + self.fib(N - 2)


# Accepted
# 31/31 cases passed (60 ms)
# Your runtime beats 31.83 % of python3 submissions
# Your memory usage beats 5.55 % of python3 submissions (13.8 MB)

# class Solution:
#     def fib(self, N: int) -> int:
#         if (N <= 1):
#             return N
#         if (N == 2):
#             return 1

#         current = 0
#         prev1 = 1
#         prev2 = 1

#         # Since range is exclusive and we want to include N, we need to put N+1.
#         for i in range(3, N+1):
#             current = prev1 + prev2
#             prev2 = prev1
#             prev1 = current
#         return current


# Accepted
# 31/31 cases passed (32 ms)
# Your runtime beats 93.14 % of python3 submissions
# Your memory usage beats 5.55 % of python3 submissions (13.7 MB)

# Contributed by LeetCode user mereck.
class Solution:
  def fib(self, N):
  	golden_ratio = (1 + 5 ** 0.5) / 2
  	return int((golden_ratio ** N + 1) / 5 ** 0.5)



# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/fibonacci-number/solution/fei-bo-na-qi-shu-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        
# @lc code=end

