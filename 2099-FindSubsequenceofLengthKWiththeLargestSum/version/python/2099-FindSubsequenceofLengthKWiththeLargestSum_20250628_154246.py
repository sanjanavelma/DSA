# Last updated: 28/06/2025, 15:42:46
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        index_num = list(enumerate(nums))
        top_k = sorted(index_num, key = lambda x: x[1], reverse = True)[:k]
        nor_k = sorted(top_k, key = lambda x : x[0])
        return [val for idx, val in nor_k]