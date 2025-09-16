# Last updated: 16/09/2025, 22:37:40
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        s = [0] * (len(gain) + 1)
        for i in range(0, len(s) - 1):
            s[i + 1] = s[i] + gain[i]
        return max(s)

        