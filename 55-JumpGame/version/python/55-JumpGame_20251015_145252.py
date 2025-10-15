# Last updated: 15/10/2025, 14:52:52
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False
        

