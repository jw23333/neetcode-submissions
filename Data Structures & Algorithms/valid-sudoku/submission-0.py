class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        def no_duplicates(values):
            seen = set()

            for value in values:
                if value == ".":
                    continue
                if value in seen:
                    return False
                seen.add(value)

            return True

        # Check each row
        for row in board:
            if not no_duplicates(row):
                return False

        # Check each column
        for col in range(9):
            values = []
            for row in range(9):
                values.append(board[row][col])

            if not no_duplicates(values):
                return False

        # Check each 3×3 square
        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):
                values = []

                for row in range(start_row, start_row + 3):
                    for col in range(start_col, start_col + 3):
                        values.append(board[row][col])

                if not no_duplicates(values):
                    return False

        return True