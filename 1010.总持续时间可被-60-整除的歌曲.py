#
# @lc app=leetcode.cn id=1010 lang=python3
#
# [1010] 总持续时间可被 60 整除的歌曲
#
from typing import List

# Time Limit Exceeded
# @lc code=start
# class Solution:
#     def numPairsDivisibleBy60(self, time: List[int]) -> int:
#         time_len = len(time)
#         i = 0
#         j = 1
#         result = 0
#         while i < time_len:
#             while j < time_len:
#                 if (time[i] + time[j])  % 60 == 0:
#                     result += 1
#                 j += 1
#             i += 1
#             j = i + 1
#         return result

# Accepted
# 34/34 cases passed (92 ms)
# Your runtime beats 91.6 % of python3 submissions
# Your memory usage beats 56.91 % of python3 submissions (17.1 MB)
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
    	# count remainder
        dic={}
        for i,t in enumerate(time):
            r = t%60
            dic.setdefault(r,0)
            dic[r]+=1
        # count cp
        count = 0
        for i in range(31):
            if i in [0,30]:
                num = dic.get(i)
                if num and num>1:
                    count+=num*(num-1)//2
            else:
                num1 = dic.get(i)
                num2 = dic.get(60-i)
                if num1 and num2:                  
                    count+=num1*num2
        return count

# 作者：tedxpy
# 链接：https://leetcode-cn.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/solution/bian-li-chao-shi-fen-xi-zheng-chu-60-yu-shu-ge-shu/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# A = Solution()
# A.numPairsDivisibleBy60([30,20,150,100,40])
# @lc code=end

