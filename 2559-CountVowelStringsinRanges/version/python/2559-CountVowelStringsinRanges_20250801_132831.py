# Last updated: 01/08/2025, 13:28:31
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix_sum = [0]
        total = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for w in words:
            if w[0] in vowels and w[-1] in vowels:
                total += 1
            prefix_sum.append(total)

        res = []
        for start, end in queries:
            res.append(prefix_sum[end + 1] - prefix_sum[start])
        return res

                
        