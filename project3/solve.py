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
        print(self.field)

    def solve_dp(self):
        print(self.field)
