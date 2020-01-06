#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

#base solution
# Accepted
# 109/109 cases passed (40 ms)
# Your runtime beats 66.92 % of python3 submissions
# Your memory usage beats 99.82 % of python3 submissions (12.7 MB)

# @lc code=start
class Solution:
    def plusOne(self, digits):
        nums_len = len(digits) - 1
        index = 0
        int_nums = 0
        return_list = list()
        while(index <= nums_len):
            int_nums += digits[index] * (10**(nums_len - index))
            index += 1
        int_nums += 1
        index = 1
        while(int_nums != 0):
            return_list.append(int_nums % 10)
            int_nums //= 10
            index += 1
        return return_list[::-1]



# Another solution reduce runtime && memory cost base on above solution
# 109/109 cases passed (28 ms)
# Your runtime beats 98.3 % of python3 submissions
# Your memory usage beats 99.82 % of python3 submissions (12.6 MB)

class Solution:
    def plus(self, nums, max_index):
        if (max_index == 0) and nums[max_index] < 9:
            nums[max_index] += 1
            return nums
        elif (max_index == 0) and nums[max_index] == 9:
            nums[max_index] = 0
            return [1] + nums
        if nums[max_index] < 9:
            nums[max_index] += 1
            return nums
        nums[max_index] = 0
        return self.plus(nums, max_index - 1)
    def plusOne(self, digits):
        nums_len = len(digits) - 1
        return self.plus(digits, nums_len)


# A = Solution()
# print (A.plusOne([9]))
# @lc code=end

