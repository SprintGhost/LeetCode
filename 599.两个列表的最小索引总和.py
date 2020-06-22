#
# @lc app=leetcode.cn id=599 lang=python3
#
# [599] 两个列表的最小索引总和
#

# Accepted
# 133/133 cases passed (236 ms)
# Your runtime beats 57.18 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13.7 MB)

# @lc code=start
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hash_temp = dict()
        for index, each in enumerate(list1):
            hash_temp[each] = index
        result = list()
        min_sum = 0xffffffff
        sum = 0
        for index,each in enumerate(list2):
            if index > min_sum:
                break
            if each in hash_temp:
                sum = index + hash_temp[each]
                if (sum < min_sum):
                    result = list()
                    result.append(each)
                    min_sum = sum
                elif (sum == min_sum):
                    result.append(each)
        return result

# @lc code=end

