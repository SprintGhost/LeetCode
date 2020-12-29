#
# @lc app=leetcode.cn id=1005 lang=python3
#
# [1005] K 次取反后最大化的数组和
#

# Accepted
# 78/78 cases passed (60 ms)
# Your runtime beats 75.32 % of python3 submissions
# Your memory usage beats 5.19 % of python3 submissions (15 MB)
# @lc code=start
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A = sorted(A)
        index = 0
        if A[0] >= 0:
            if K % 2 == 0:
                return sum(A)
            else:
                return sum(A[1:]) - A[0]
        else:
            while (K > 0) and (index < len(A)):
                if A[index] >= 0:
                    break
                else:
                    A[index] = -1 * A[index]
                    K = K - 1
                index += 1
        
        if K > 0 and K % 2 != 0:
            if A[index] > A[index -1]: 
                A[index -1] = -1 * A[index - 1]
            else:
                A[index] = -1 * A[index]
        return sum(A)

        
# Another good sulution written by Java. 

# class Solution {
#      public int largestSumAfterKNegations(int[] A, int K) {
#         int[] number = new int[201];//-100 <= A[i] <= 100,这个范围的大小是201
#         for (int t : A) {
#             number[t + 100]++;//将[-100,100]映射到[0,200]上
#         }
#         int i = 0;
#         while (K > 0) {
#             while (number[i] == 0)//找到A[]中最小的数字
#                 i++;
#             number[i]--;//此数字个数-1
#             number[200 - i]++;//其相反数个数+1
#             if (i > 100) {//若原最小数索引>100,则新的最小数索引应为200-i.(索引即number[]数组的下标)
#                 i = 200 - i;
#             }
#             K--;
#         }
#         int sum = 0;
#         for (int j = i; j <number.length ; j++) {//遍历number[]求和
#             sum += (j-100)*number[j];//j-100是数字大小,number[j]是该数字出现次数.
#         }
#         return sum;
#     }
# }

# 作者：FlyChenKai
# 链接：https://leetcode-cn.com/problems/maximize-sum-of-array-after-k-negations/solution/java-chao-yue-9966xiang-xi-jie-xi-by-flychenkai/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# @lc code=end

