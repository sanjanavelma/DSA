# Last updated: 16/08/2025, 13:02:15
class Solution:
    def maximum69Number (self, num: int) -> int:
        num_copy = num
        index_first_six = -1
        curr_digit = 0
        while num_copy > 0:
            if num_copy % 10 == 6:
                index_first_six = curr_digit
            num_copy //= 10
            curr_digit += 1
        return num if index_first_six == -1 else num + 3 * 10 ** index_first_six


        