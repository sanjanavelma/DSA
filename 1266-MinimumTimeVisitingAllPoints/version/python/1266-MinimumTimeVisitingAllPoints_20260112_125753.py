# Last updated: 12/01/2026, 12:57:53
1class Solution:
2    def minTimeToVisitAllPoints(self, p: List[List[int]]) -> int:
3        Ans = 0
4        for i in range(1, len(p)):
5            Ans += max(
6                abs(p[i][0] - p[i - 1][0]),
7                abs(p[i][1] - p[i - 1][1])
8            )
9        return Ans
10        