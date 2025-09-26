# Last updated: 26/09/2025, 14:32:47
class Solution:
    def removeStars(self, s: str) -> str:
        ans = []
        for i in s:
            if i == '*':
                ans.pop()
            else:
                ans += [i]
        return "".join(ans)
        