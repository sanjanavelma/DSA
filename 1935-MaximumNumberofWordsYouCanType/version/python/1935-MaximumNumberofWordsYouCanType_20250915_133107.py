# Last updated: 15/09/2025, 13:31:07
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        counter = 0
        for word in text.split():
            for letter in word:
                if letter in brokenLetters:
                    counter+=1
                    break
        return len(text.split())-counter
        