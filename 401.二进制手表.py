#
# @lc app=leetcode.cn id=401 lang=python3
#
# [401] 二进制手表
#

# Accepted
# 10/10 cases passed (40 ms)
# Your runtime beats 62.11 % of python3 submissions
# Your memory usage beats 5.88 % of python3 submissions (13.7 MB)

# @lc code=start
class Solution:
    def count(self,n):
        res = 0
        while(n):
            n &= (n -1)
            res += 1
        return res
    def readBinaryWatch(self, num: int) -> List[str]:
        counter = list()
        result = list()
        for index in range(0 , 60):
            counter.append(self.count(index))
        
        for index_i in range(0,12):
            for index_j in range(0,60):
                if (counter[index_j] + counter[index_i] == num):
                    result.append(str(index_i) + ":" + (str(index_j) if index_j > 9 else ("0" + str(index_j))))

        return result     

        
# @lc code=end

