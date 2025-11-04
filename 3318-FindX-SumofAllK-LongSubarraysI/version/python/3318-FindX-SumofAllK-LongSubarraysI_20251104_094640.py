# Last updated: 04/11/2025, 09:46:40
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        result = []
        for i in range(n - k + 1):
            w = nums[i:i + k]
            f = Counter(w)
            sort = sorted(f.items(), key=lambda a: (-a[1], -a[0]))
            t = set(num for num, _ in sort[:x])
            x_sum = sum(num for num in w if num in t)
            result.append(x_sum)
        return result

        