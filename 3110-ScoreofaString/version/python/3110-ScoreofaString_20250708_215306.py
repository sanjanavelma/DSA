# Last updated: 08/07/2025, 21:53:06
class Solution:
    def scoreOfString(self, s: str) -> int:
        num = [ord(i) for i in s]
        add = 0
        for i in range(len(num) - 1):
            add += abs(num[i] - num[i + 1])
        return add