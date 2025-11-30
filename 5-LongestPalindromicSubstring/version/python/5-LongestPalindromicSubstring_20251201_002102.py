# Last updated: 01/12/2025, 00:21:02
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        ans = ''
4        for i in range(len(s)):
5            ans = max(ans, expand(s, i, i), expand(s, i, i+1), key=len)
6        return ans
7
8def expand(s, i, j):
9    while i >= 0 and j <len(s) and s[i] == s[j]:
10        i -= 1
11        j += 1
12    return s[i+1:j]
13
14        