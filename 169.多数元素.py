#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# Accepted
# 44/44 cases passed (192 ms)
# Your runtime beats 80.9 % of python3 submissions
# Your memory usage beats 51.91 % of python3 submissions (14.3 MB)

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_dict = dict()
        for i in nums:
            if i in num_dict:
                num_dict[i] += 1
            else:
                num_dict[i] = 0
        temp = -1
        result = -1
        for each in num_dict:
            if num_dict[each] > temp:
                result = each
                temp = num_dict[each]
        return result

# Accepted
# 44/44 cases passed (192 ms)
# Your runtime beats 80.9 % of python3 submissions
# Your memory usage beats 51.87 % of python3 submissions (14.4 MB)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]

# Accepted
# 44/44 cases passed (192 ms)
# Your runtime beats 80.9 % of python3 submissions
# Your memory usage beats 51.83 % of python3 submissions (14.4 MB)

class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/majority-element/solution/qiu-zhong-shu-by-leetcode-2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# @lc code=end

