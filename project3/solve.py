# Helper function to parse the input (soccer field) as a 2D grid.
def get_input(file_name) -> list[str]:
    res = []
    with open(file_name, "r") as f:
        res = f.read().strip().split("\n")
    return res


# A class with methods solve_exhaustive and solve_dp that solves
# The Opponent Avoidance Problem using exhaustive search and DP.
class Solve:
    field = get_input("input.txt")

    def solve_exhaustive(self) -> int:
        # Initialize r and c as the # of rows and columns
        r, c = len(self.field), len(self.field[0])
        size = r + c - 2
        output = 0

        # Loop through 0 to 2^n - 1
        for bits in range(pow(2, size)):
            # Capture all the moves in candidate
            candidate = []
            # Loop through 0 to size - 1
            for k in range(size):
                # Interpret the bit at position k
                # as either 0 (down) or 1 (right)
                bit = (bits >> k) & 1
                if bit == 1:
                    candidate.append("R")
                else:
                    candidate.append("D")

            # Test whether the candidate path stays inside the
            # grid, never crosses "X", and ends at (r - 1, c - 1)
            # If all conditions meet, increment output by 1
            curr_row = curr_col = 0
            for move in candidate:
                curr_col += 1 if move == "R" else 0
                curr_row += 1 if move == "D" else 0
                if (
                    curr_row >= r
                    or curr_col >= c
                    or self.field[curr_row][curr_col] == "X"
                ):
                    break
            if curr_row == r - 1 and curr_col == c - 1:
                output += 1

        # Return the number of paths
        return output

    def solve_dp(self) -> int:
        # Edge case: initial cell is impassible
        if self.field[0][0] == "X":
            return 0

        # Initialize r and c as the # of rows and columns
        r, c = len(self.field), len(self.field[0])
        # Let paths = new r x c matrices initialized with 0s
        paths = [[0 for _ in range(c)] for _ in range(r)]
        paths[0][0] = 1

        # Loop through each index in the grid
        for i in range(r):
            for j in range(c):
                # If the cell is occupied, it cannot be reached
                if self.field[i][j] == "X":
                    paths[i][j] = 0
                    continue

                above = left = 0
                # Look above and see if the (i - 1, j) is a "."
                if i > 0 and self.field[i - 1][j] == ".":
                    above = paths[i - 1][j]
                # Look to the left and see if the (i, j - 1) is a "."
                if j > 0 and self.field[i][j - 1] == ".":
                    left = paths[i][j - 1]
                # Update paths at (i, j) from the above and left
                paths[i][j] += above + left

        # Return the number of paths to the bottom right corner
        return paths[r - 1][c - 1]

    def print_grid(self) -> None:
        for line in self.field:
            print(line)
        print()
