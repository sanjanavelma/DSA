# Last updated: 19/06/2025, 21:18:38
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        string = [word[::-1] for word in words]
        return " ".join(string)

          

        