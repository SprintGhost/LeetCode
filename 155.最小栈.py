#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈

# Accepted
# 18/18 cases passed (60 ms)
# Your runtime beats 95.33 % of python3 submissions
# Your memory usage beats 5.22 % of python3 submissions (17.7 MB)#


# @lc code=start
class MinStack:

    class node:
        def __init__(self):
            self.val = 0
            self.next = None

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.start = None
        self.min = 0xFFFFFFFF

    def push(self, x: int) -> None:
        if (x < self.min) or (x == self.min):
            temp_min = self.node()
            temp_min.val = self.min
            temp_min.next = self.start
            self.start = temp_min
            self.min = x      
        temp = self.node()
        temp.val = x
        temp.next = self.start
        self.start = temp

    def pop(self) -> None:
        if not self.start:
            return
        if self.min == self.start.val:
            self.start = self.start.next
            self.min = self.start.val
        self.start = self.start.next

    def top(self) -> int:
        if not self.start:
            return
        return self.start.val

    def getMin(self) -> int:
        if not self.start:
            return
        return self.min


# Accepted
# 18/18 cases passed (72 ms)
# Your runtime beats 65.31 % of python3 submissions
# Your memory usage beats 5.22 % of python3 submissions (17.7 MB)

class MinStack:

    class node:
        def __init__(self,val,min):
            self.val = val
            self.next = None
            self.min = min

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.start = None

    def push(self, x: int) -> None:
        if not self.start:
            self.start = self.node(x, x)
        else:
            temp = self.node(x, min(x, self.start.min))
            temp.next = self.start
            self.start = temp

    def pop(self) -> None:
        if self.start:
            self.start = self.start.next
    

    def top(self) -> int:
        if self.start:
            return self.start.val
        return None

    def getMin(self) -> int:
        if self.start:
            return self.start.min
        return None

# 作者：windliang
# 链接：https://leetcode-cn.com/problems/min-stack/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-38/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(4)
# obj.pop()
# param_3 = obj.top()
# print (param_3)
# param_4 = obj.getMin()
# @lc code=end

