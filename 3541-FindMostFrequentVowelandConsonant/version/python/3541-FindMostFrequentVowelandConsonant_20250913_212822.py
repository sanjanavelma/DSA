# Last updated: 13/09/2025, 21:28:22
class Solution:
    def maxFreqSum(self, s: str) -> int:
        v_max = 0
        c_max = 0
        v = 'aeiou'
        c = Counter(s)
        for i in c:
            if i in v:
                v_max = max(v_max, c[i])
            else:
                c_max = max(c_max, c[i])
        return v_max + c_max

        