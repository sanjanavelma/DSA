# Last updated: 09/07/2025, 21:12:59
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_final = -1
        for i in range(len(arr) - 1, -1, -1):
            current = arr[i]
            arr[i] = max_final
            max_final = max(current, max_final)
        return arr
                

        