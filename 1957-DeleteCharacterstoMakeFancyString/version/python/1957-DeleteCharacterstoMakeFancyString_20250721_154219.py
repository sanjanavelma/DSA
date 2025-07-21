# Last updated: 21/07/2025, 15:42:19
class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []
        last = s[0]
        result.append(last)
        count = 1
        for i in range(1, len(s)):
            if s[i] == last:
                count += 1
                if count < 3:
                    result.append(s[i])
            else:
                last = s[i]
                count = 1
                result.append(s[i])
        return "".join(result)