# Last updated: 12/09/2025, 20:54:20
class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split(' ')
        l = [i for i in l if i!= '']
        return ' '.join(l[::-1])
        