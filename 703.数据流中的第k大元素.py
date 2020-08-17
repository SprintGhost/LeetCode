#
# @lc app=leetcode.cn id=703 lang=python3
#
# [703] 数据流中的第K大元素
#

# Accepted
# 10/10 cases passed (112 ms)
# Your runtime beats 96.27 % of python3 submissions
# Your memory usage beats 48.78 % of python3 submissions (17.8 MB)

# @lc code=start
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        while len(self.nums) > k :
            heapq.heappop(self.nums)


    def add(self, val: int) -> int:
        heapq.heappush(self.nums,val)
        if len(self.nums) > self.k :
            heapq.heappop(self.nums)
        return self.nums[0]

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

