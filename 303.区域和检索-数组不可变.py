#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#

# Accepted
# 16/16 cases passed (3788 ms)
# Your runtime beats 5.01 % of python3 submissions
# Your memory usage beats 8.23 % of python3 submissions (17 MB)

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums_list = nums
        

    def sumRange(self, i: int, j: int) -> int:
        sum = 0
        for each in self.nums_list[i:j+1]:
            sum += each
        return sum


# Accepted
# 16/16 cases passed (88 ms)
# Your runtime beats 86.33 % of python3 submissions
# Your memory usage beats 8.23 % of python3 submissions (17 MB)

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums_list = list()
        self.nums_list.append(0)
        for index, each in enumerate(nums):
            self.nums_list.append(self.nums_list[index] + each)

        

    def sumRange(self, i: int, j: int) -> int:
        return self.nums_list[j + 1] - self.nums_list[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
# @lc code=end

