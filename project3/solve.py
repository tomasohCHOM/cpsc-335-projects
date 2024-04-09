# Helper function to parse the input (soccer field) as a 2D grid.
def get_input(file_name):
    res = []
    with open(file_name, "r") as f:
        res = f.read().strip().split("\n")
    return res


# A static class with methods solve_exhaustive and solve_dp that
# solves the opponent avoidance problem using exhaustive search and DP.
class Solve:
    field = get_input("input.txt")

    def solve_exhaustive(self):
        r, c = len(self.field), len(self.field[0])
        size = r + c - 2
        output = 0
        for bits in range(pow(2, size)):
            candidate = []
            for k in range(size):
                bit = (bits >> k) & 1
                if bit == 1:
                    candidate.append("R")
                else:
                    candidate.append("D")
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
        return output

    def solve_dp(self):
        # Edge case: initial cell is impassible
        if self.field[0][0] == "X":
            return 0
        r, c = len(self.field), len(self.field[0])
        area = [[0 for _ in range(c)] for _ in range(r)]
        area[0][0] = 1
        for i in range(r):
            for j in range(c):
                if self.field[i][j] == "X":
                    area[i][j] = 0
                    continue
                above = left = 0
                if i > 0 and self.field[i - 1][j] == ".":
                    above = area[i - 1][j]
                if j > 0 and self.field[i][j - 1] == ".":
                    left = area[i][j - 1]
                area[i][j] += above + left
        return area[r - 1][c - 1]

    def print_grid(self):
        for line in self.field:
            print(line)
        print()
