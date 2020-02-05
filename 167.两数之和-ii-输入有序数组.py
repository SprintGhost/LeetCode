#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# Accepted
# 17/17 cases passed (100 ms)
# Your runtime beats 19.7 % of python3 submissions
# Your memory usage beats 52.64 % of python3 submissions (13.7 MB)

# Difference test case has difference result

# Accepted
# 17/17 cases passed (64 ms)
# Your runtime beats 91.37 % of python3 submissions
# Your memory usage beats 52.64 % of python3 submissions (13.8 MB)

# @lc code=start
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         hash_table = {}
#         for index, num in enumerate(numbers):
#             another_number = target - num
#             if another_number in hash_table:
#                 return [hash_table[another_number], index + 1]
#             hash_table[num] = index + 1
#         return None

#  The following solution use less space

# Accepted
# 17/17 cases passed (76 ms)
# Your runtime beats 58.67 % of python3 submissions
# Your memory usage beats 52.64 % of python3 submissions (13.6 MB)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low_index = 0
        high_pindex = len(numbers) - 1
        while(low_index < high_pindex):
            num = numbers[low_index] + numbers[high_pindex]
            if num == target:
                return [low_index + 1, high_pindex + 1]
            elif num > target:
                high_pindex -= 1
            else:
                low_index += 1
        return None

# @lc code=end

