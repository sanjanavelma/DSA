# Last updated: 19/10/2025, 23:22:27
class Solution:
    def convert(self, s: str, numRow: int) -> str:
        if numRow == 1 or numRow >= len(s):
            return s
        idx, d = 0, 1
        rows = [[] for _ in range(numRow)]
        for char in s:
            rows[idx].append(char)
            if idx == 0:
                d = 1
            elif idx == numRow - 1:
                d = -1
            idx += d
        for i in range(numRow):
            rows[i] = ''.join(rows[i])
        return ''.join(rows)
        