#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#

# Accepted
# 16/16 cases passed (36 ms)
# Your runtime beats 46.95 % of python3 submissions
# Your memory usage beats 28.33 % of python3 submissions (13.4 MB)

# @lc code=start
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = list()


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.stack.insert(0,x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.stack.pop(0)


    def top(self) -> int:
        """
        Get the top element.
        """
        return self.stack[0]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return (len(self.stack) == 0)



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

