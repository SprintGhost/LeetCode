#
# @lc app=leetcode.cn id=506 lang=python3
#
# [506] 相对名次
#

# Accepted
# Accepted
# 17/17 cases passed (484 ms)
# Your runtime beats 19.64 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (14.6 MB)

# @lc code=start
class Solution:
    def findRelativeRanks(self, nums):
        nums_len = len(nums)
        sorted_nums = sorted(nums)
        result = [-1] * nums_len
        for index, each in enumerate(sorted_nums):
            each_in_nums_index = nums.index(each)
            if index < (nums_len - 3):
                result[each_in_nums_index] = str(nums_len - index)
            elif index == nums_len - 1:
                result[each_in_nums_index] = "Gold Medal"
            elif index == nums_len - 2:
                result[each_in_nums_index] = "Silver Medal"
            else:
                result[each_in_nums_index] = "Bronze Medal"
                
        return result
# Accepted
# 17/17 cases passed (96 ms)
# Your runtime beats 59.72 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (14.6 MB)

        s,dic,start = sorted(nums,reverse=True),{},1
        for i,val in enumerate(s):
            if start == 1:
                dic[val] = "Gold Medal"
            if start == 2:
                dic[val] = "Silver Medal"
            if start == 3:
                dic[val] = "Bronze Medal"
            if start > 3:
                dic[val] = str(start)
            start+=1
        res = []
        for i in range(len(nums)):
            res.append(dic.get(nums[i]))
        return res


# 作者：metachuan
# 链接：https://leetcode-cn.com/problems/relative-ranks/solution/xiang-dui-ming-ci-by-user5475/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# @lc code=end

