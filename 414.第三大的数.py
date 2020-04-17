#
# @lc app=leetcode.cn id=414 lang=python3
#
# [414] 第三大的数
#

# Accepted
# 26/26 cases passed (64 ms)
# Your runtime beats 65.96 % of python3 submissions
# Your memory usage beats 16.67 % of python3 submissions (14.9 MB)

# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        if len(nums) < 3:
            return nums[-1]
        else:
            return nums[-3]

# Accepted
# 26/26 cases passed (60 ms)
# Your runtime beats 79.37 % of python3 submissions
# Your memory usage beats 16.67 % of python3 submissions (14.7 MB)

# Good sulution
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = float('-inf')
        for num in nums:
            if num > third:
                if num < second:
                    third = num
                elif num > second:
                    if num < first:
                        third = second
                        second = num
                    elif num > first:
                        third = second
                        second = first
                        first = num
        if third == float('-inf'):
            return first
        else:
            return third


# 作者：erik_chen
# 链接：https://leetcode-cn.com/problems/third-maximum-number/solution/an-zhao-gai-lu-da-xiao-you-hua-if-elif-fen-zhi-yu-/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。       
# @lc code=end

