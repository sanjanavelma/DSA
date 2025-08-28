# Last updated: 28/08/2025, 13:50:10
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sort_h = sorted(heights)
        count = 0
        for i in range(0, len(heights)):
            if sort_h[i] != heights[i]:
                count += 1
        return count
        