# Last updated: 01/08/2025, 10:32:45
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(numRows - 1):
            code = [0] + res[-1] + [0]
            fin = []
            for j in range(len(res[-1]) + 1):
                fin.append(code[j] + code[j + 1])
            res.append(fin)
        return res