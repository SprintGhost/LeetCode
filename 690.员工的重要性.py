#
# @lc app=leetcode.cn id=690 lang=python3
#
# [690] 员工的重要性
#

# @lc code=start

# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        temp = {e.id: e for e in employees}
        def find(id):
            e_temp = temp[id]
            return (e_temp.importance + sum(find(sub_id) for sub_id in e_temp.subordinates))
        return find(id)

# Accepted
# 108/108 cases passed (184 ms)
# Your runtime beats 58.75 % of python3 submissions
# Your memory usage beats 25 % of python3 submissions (14.8 MB)

# @lc code=end

