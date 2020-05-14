#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# Accepted
# 17/17 cases passed (88 ms)
# Your runtime beats 43.72 % of python3 submissions
# Your memory usage beats 25 % of python3 submissions (13.8 MB)

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = list()
        nums2_len = len(nums2)
        flag = True
        for each in nums1:
            each_index_in_nums2 = nums2.index(each)
            if (each_index_in_nums2 == (nums2_len - 1)):
                result.append(-1)
                continue
            for index in range(each_index_in_nums2 + 1, nums2_len):
                temp = nums2[index]
                if  temp > each:
                    result.append(temp)
                    flag = False
                    break
            if flag:
                result.append(-1)
            flag = True
        return result       

# Accepted
# 17/17 cases passed (68 ms)
# Your runtime beats 59.58 % of python3 submissions
# Your memory usage beats 25 % of python3 submissions (13.9 MB)

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, hashmap = list(), dict()
        for i in nums2:
            while len(stack) != 0 and stack[-1] < i:
                hashmap[stack.pop()] = i
            stack.append(i)
        return [hashmap.get(i,-1) for i in nums1]

# 作者：qsctech-sange
# 链接：https://leetcode-cn.com/problems/next-greater-element-i/solution/python3-wu-xing-dai-ma-di-jian-zhan-ha-xi-biao-by-/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# @lc code=end

