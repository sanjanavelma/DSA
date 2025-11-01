# Last updated: 02/11/2025, 01:53:10
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        mp = {}
        res = 0
        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res