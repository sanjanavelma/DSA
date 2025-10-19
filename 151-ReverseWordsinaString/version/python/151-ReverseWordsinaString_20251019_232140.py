# Last updated: 19/10/2025, 23:21:40
class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split(' ')
        l = [i for i in l if i!= '']
        return ' '.join(l[::-1])
        