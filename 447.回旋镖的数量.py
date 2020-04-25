#
# @lc app=leetcode.cn id=447 lang=python3
#
# [447] 回旋镖的数量
#
# Accepted
# 31/31 cases passed (1312 ms)
# Your runtime beats 72.17 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13.6 MB)
# @lc code=start
import collections
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans=0
        for i in points:
            dis=[]
            for j in points:
                dis.append((j[1]-i[1])**2+(j[0]-i[0])**2)
            for j,k in collections.Counter(dis).items():
                if j!=0 and k>=2:ans+=k*(k-1)
        return ans

# 作者：jutraman
# 链接：https://leetcode-cn.com/problems/number-of-boomerangs/solution/pythonhui-xuan-biao-de-shu-liang-by-jutraman/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
 
# @lc code=end

