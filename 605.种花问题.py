#
# @lc app=leetcode.cn id=605 lang=python3
#
# [605] 种花问题
#

# Accepted
# 123/123 cases passed (204 ms)
# Your runtime beats 68.07 % of python3 submissions
# Your memory usage beats 10 % of python3 submissions (13.9 MB)

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        index = 0
        count = 0
        sub_len = len(flowerbed)
        while (index < sub_len):
            if (flowerbed[index] == 0 and (index == 0 or flowerbed[index - 1] == 0) and (index == sub_len - 1 or flowerbed[index + 1] == 0)):
                flowerbed[index] = 1
                count += 1
            if count >= n:
                return True
            index += 1

        return False

# Accepted
# 123/123 cases passed (260 ms)
# Your runtime beats 17.19 % of python3 submissions
# Your memory usage beats 10 % of python3 submissions (13.9 MB)



# @lc code=end

