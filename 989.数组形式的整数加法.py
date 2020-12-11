#
# @lc app=leetcode.cn id=989 lang=python3
#
# [989] 数组形式的整数加法
#
# Accepted
# 156/156 cases passed (280 ms)
# Your runtime beats 99.05 % of python3 submissions
# Your memory usage beats 5.09 % of python3 submissions (15.4 MB)
# @lc code=start
class Solution:
    def addToArrayForm(self, A, K: int):
        carry_bit = 0
        index = len(A) - 1
        add_value = 0
        while K > 0 or (carry_bit == 1 and index > -1 ):
            temp = K % 10
            K = K // 10
            if (index > -1):
                add_value = temp + A[index] + carry_bit 
                carry_bit = 0
                if add_value < 10:
                    A[index] = add_value
                else:
                    carry_bit = 1
                    A[index] = add_value - 10
                index -= 1
            else:
                add_value = temp + carry_bit
                carry_bit = 0
                if add_value < 10:
                    if index > -1:
                        A.insert(index,add_value)
                    else:
                        A.insert(0,add_value)
                else:
                    if index > -1:
                        A.insert(index, add_value - 10)
                    else:
                        A.insert(0,add_value - 10)
                    carry_bit = 1
        # while carry_bit == 1 and index > -1 :
        #     add_value = A[index] + carry_bit
        #     carry_bit = 0
        #     if add_value < 10:
        #         A[index] = add_value
        #     else:
        #         carry_bit = 1
        #         A[index] = add_value - 10
        #     index -= 1
        if carry_bit == 1:
            A.insert(0,carry_bit)
        return A

# Accepted
# 156/156 cases passed (292 ms)
# Your runtime beats 97.9 % of python3 submissions
# Your memory usage beats 5.09 % of python3 submissions (15.4 MB)
class Solution(object):
    def addToArrayForm(self, A, K):
        A[-1] += K
        for i in range(len(A) - 1, -1, -1):
            carry, A[i] = divmod(A[i], 10)
            if i: A[i-1] += carry
        if carry:
            A = list(map(int, str(carry))) + A
        return A

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/add-to-array-form-of-integer/solution/shu-zu-xing-shi-de-zheng-shu-jia-fa-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# B = Solution()
# print (B.addToArrayForm([7],993))

        
        
# @lc code=end

