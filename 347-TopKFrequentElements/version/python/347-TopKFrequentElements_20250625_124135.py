# Last updated: 25/06/2025, 12:41:35
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) +1)]
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cun in count.items():
            freq[cun].append(num)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res