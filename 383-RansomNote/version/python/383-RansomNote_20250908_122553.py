# Last updated: 08/09/2025, 12:25:53
class Solution:
    def canConstruct(self, ran: str, mag: str) -> bool:
        c1 = Counter(mag)
        c2 = Counter(ran)
        for i in c2:
            if c1[i] < c2[i]:
                return False
        return True
