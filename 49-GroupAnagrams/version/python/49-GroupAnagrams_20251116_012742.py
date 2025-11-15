# Last updated: 16/11/2025, 01:27:42
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = {}
        for i in strs:
            s = ''.join(sorted(i))
            if s in a:
                a[s].append(i)
            else:
                a[s] = [i]
        res = list(a.values())
        return res
        