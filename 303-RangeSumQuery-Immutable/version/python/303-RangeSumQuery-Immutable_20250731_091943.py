# Last updated: 31/07/2025, 09:19:43
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        sum = 0
        for n in nums:
            sum += n
            self.prefix.append(sum)        

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix[right]
        else:
            return self.prefix[right] - self.prefix[left - 1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)