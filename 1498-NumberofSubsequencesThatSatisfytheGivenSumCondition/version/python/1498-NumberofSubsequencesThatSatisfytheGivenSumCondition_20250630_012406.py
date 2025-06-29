# Last updated: 30/06/2025, 01:24:06
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        result = 0
        nums.sort()
        power = [1] * n
        for i in range(1, n):
            power[i] = (power[i - 1] * 2) % MOD
        l = 0
        r = n - 1
        while l <= r:
            if nums[l] + nums[r] <= target:
                result += power[r - l]
                result %= MOD
                l += 1
            else:
                r -= 1

        return result