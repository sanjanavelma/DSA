// Last updated: 17/06/2025, 22:14:42
class Solution {
    public boolean isValidRange(char[][] board, int rowStart, int rowEnd, int colStart, int colEnd) {
        boolean[] numUsed = new boolean[10];

        for (int row = rowStart; row <= rowEnd; row++) {
            for (int col = colStart; col <= colEnd; col++) {
                if (board[row][col] != '.') {
                    if (numUsed[board[row][col] - '0']) {
                        return false;
                    }

                    numUsed[board[row][col] - '0'] = true;
                }
            }
        }

        return true;
    }

    public boolean isValidSudoku(char[][] board){
        for (int row = 0; row <= 8; row++) {
            if (! isValidRange(board, row, row, 0, 8)) {
                return false;
            }
        }
        for (int col = 0; col <= 8; col++) {
            if (! isValidRange(board, 0, 8, col, col)) {
                return false;
            }
        }
        for (int i = 0; i <=2; i++) {
            for (int j = 0; j <= 2; j++) {
                if (! isValidRange(board, i*3, i*3+2, j*3, j*3 +2)) {
                    return false;
                }
             }
        }

        return true;
    }
}