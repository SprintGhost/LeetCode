#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#


# Accepted
# 1101/1101 cases passed (40 ms)
# Your runtime beats 48.03 % of python3 submissions
# Your memory usage beats 9.55 % of python3 submissions (13.6 MB)

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        while(num >= 10):
            sum_result = 0
            while(num > 0):
                sum_result += num % 10
                num = num // 10
            num = sum_result
        return num


# Accepted
# 1101/1101 cases passed (56 ms)
# Your runtime beats 10.91 % of python3 submissions
# Your memory usage beats 9.81 % of python3 submissions (13.5 MB)
        # x * 100 + y * 10 + z = z * 99 + y * 9 + x + y + z
        if num == 0:
            return 0
        return (num - 1) % 9 + 1
    # 作者：liveforexperience
    # 链接：https://leetcode-cn.com/problems/add-digits/solution/java-o1jie-fa-de-ge-ren-li-jie-by-liveforexperienc/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



# A = Solution()
# print(A.addDigits(38))
# @lc code=end

