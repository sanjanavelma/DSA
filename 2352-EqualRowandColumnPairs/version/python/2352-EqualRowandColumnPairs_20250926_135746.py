# Last updated: 26/09/2025, 13:57:46
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_counts = defaultdict(int)
        for row in grid:
            row_counts[tuple(row)] += 1
        count = 0
        for c in range(n):
            col = []
            for r in range(n):
                col.append(grid[r][c])
            col_tuple = tuple(col)
            count += row_counts[col_tuple]
        return count