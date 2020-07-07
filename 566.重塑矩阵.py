#
# @lc app=leetcode.cn id=566 lang=python3
#
# [566] 重塑矩阵
#

# Accepted
# 56/56 cases passed (124 ms)
# Your runtime beats 53.39 % of python3 submissions
# Your memory usage beats 33.33 % of python3 submissions (14.9 MB)

# @lc code=start
class Solution:
    def matrixReshape(self, nums, r: int, c: int):
        result = list()
        temp = list()
        temp_c = c
        for each in nums:
            if r < 0:
                return nums
            for each_c in each:
                if c > 0:
                    temp.append(each_c)
                    c -= 1
                    if c == 0:
                        result.append(temp.copy())
                        temp = list()
                        r -= 1
                        c = temp_c
                else:
                    result.append(temp.copy())
                    temp = list()
                    r -= 1
                    c = temp_c
        
        if r > 0 or ((c != temp_c) and (c > 0)):
            return nums
        return result

# Accepted
# 56/56 cases passed (112 ms)
# Your runtime beats 91.97 % of python3 submissions
# Your memory usage beats 33.33 % of python3 submissions (14.5 MB)

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        m,n=len(nums),len(nums[0])
        if m*n!=r*c:
            return nums
        res=[i for j in nums for i in j]    
        return [res[i:i+c] for i in range(0,len(res),c)]

# 作者：2558260433
# 链接：https://leetcode-cn.com/problems/reshape-the-matrix/solution/pythonqie-pian-hao-yong-by-2558260433/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# A = Solution()
# A.matrixReshape([[1,2],[3,4]], 1, 4)      
# @lc code=end

