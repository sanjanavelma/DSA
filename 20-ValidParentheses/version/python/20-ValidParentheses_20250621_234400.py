# Last updated: 21/06/2025, 23:44:00
class Solution:
    def isValid(self, s: str) -> bool:

        dictt = {")": "(", "]": "[", "}": "{"}
        stack = []
        for x in s:
            if x in dictt:
                top_element = stack.pop() if stack else "*"
                if dictt[x] != top_element:
                    return False
            else:
                stack.append(x)
                
        if len(stack) == 0:
            return True
        else:
            return False




        