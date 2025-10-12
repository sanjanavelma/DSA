# Last updated: 12/10/2025, 21:53:03
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        output_str = ''
        for i in range(len(strs[0])):
            x = strs[0][i]
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != x:
                    return output_str
            output_str += x
        return output_str