# Last updated: 28/07/2025, 21:59:37
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        self.max_or = 0
        self.count = 0

        def dfs(i, curr_or):
            if i == len(nums):
                if curr_or == self.max_or:
                    self.count += 1
                elif curr_or > self.max_or:
                    self.max_or = curr_or
                    self.count = 1
                return
            

            dfs(i + 1, curr_or | nums[i])


            dfs(i + 1, curr_or)

        dfs(0, 0)
        return self.count
