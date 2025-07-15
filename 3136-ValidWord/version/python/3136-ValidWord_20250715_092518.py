# Last updated: 15/07/2025, 09:25:18
class Solution:
    def isValid(self, word: str) -> bool:
        vowel_set = "aeiouAEIOU"
        vowel = 0
        cons = 0
        if len(word) < 3:
            return False
        for c in word:
            if c.isalpha():
                if c in vowel_set:
                    vowel += 1
                else:
                    cons += 1
            elif not c.isdigit():
                return False
        return vowel >= 1 and cons >= 1

        