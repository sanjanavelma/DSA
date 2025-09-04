# Last updated: 04/09/2025, 14:09:14
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total = 0
        car = Counter(chars)
        for i in words:
            char = Counter(i)
            if all(char[c] <= car[c] for c in char):
                total += len(i)
        return total


        