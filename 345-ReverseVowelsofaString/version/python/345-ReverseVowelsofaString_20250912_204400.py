# Last updated: 12/09/2025, 20:44:00
class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r = 0, len(s) - 1
        v = 'aeiouAEIOU'
        w = list(s)
        while l <= r:
            while l < r and v.find(w[l]) == -1:
                l += 1
            while l < r and v.find(w[r]) == -1:
                r -= 1
            w[l], w[r] = w[r], w[l]
            l += 1
            r -= 1
        return "".join(w)

            
        