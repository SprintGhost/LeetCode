#
# @lc app=leetcode.cn id=475 lang=python3
#
# [475] 供暖器
#
# Accepted
# 30/30 cases passed (360 ms)
# Your runtime beats 75.79 % of python3 submissions
# Your memory usage beats 9.09 % of python3 submissions (16.9 MB)
# @lc code=start
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.append(float("inf"))
        heaters.sort()
        max_dist = 0
        index = 0
        for house in houses:
            while (house >= heaters[index]):
                index += 1
            if index > 0: 
                curr_dist = min(heaters[index] - house, house - heaters[index-1])
            else:
                curr_dist = abs(heaters[index] - house)
            max_dist = max(max_dist, curr_dist)
                
        return max_dist

# A = Solution()
# A.findRadius([1,2,3,4],[1,4])
# @lc code=end

