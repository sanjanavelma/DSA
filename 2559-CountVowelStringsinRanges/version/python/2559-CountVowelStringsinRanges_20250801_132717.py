# Last updated: 01/08/2025, 13:27:17
class Solution:
    def isVowel(self, ch: str) -> bool:
        vowels = 'aeiou'
        return ch in vowels

    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        pre = [0] * n
        for i in range(n):
            temp = words[i]
            if self.isVowel(temp[0]) and self.isVowel(temp[-1]):
                pre[i] += 1
        for i in range(1, n):
            pre[i] += pre[i - 1]
        ans = []
        for l, r in queries:
            if l == 0:
                ans.append(pre[r])
            else:
                ans.append(pre[r] - pre[l - 1])
        return ans

            
        