# Last updated: 10/08/2025, 23:22:33
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def count_digits(x):
            return ''.join(sorted(str(x)))

        target = count_digits(n)
        
        # Precompute all powers of 2 within range
        for i in range(31):  # 2^0 to 2^30
            if count_digits(1 << i) == target:
                return True
        return False