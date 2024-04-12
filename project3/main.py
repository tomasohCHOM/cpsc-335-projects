# Name: Tomas Oh
# CSUF Email: tomasoh@csu.fullerton.edu
# CWID: 885566877
# Submission is for Project 3 of CPSC 335 (Section 04)

# Optional formatting libraries (tqdm and rich)
try:
    from tqdm import tqdm

    prog = True
except Exception:
    prog = False
    print("tdqm not found, will not show progress bar (pip install tqdm)")
try:
    from rich import print
except Exception:
    print("Rich not found, using default print (pip install rich)")


from solve import Solve

# Import datetime for creating randomness
from datetime import datetime

# Import random to generate inputs
import random as r

# Import function to time the execution
from time import time

# Import plotting library
import matplotlib.pyplot as plt

# Import sys to pipe final results to a file
import sys


# -------------------------------------------------------------------------------
# CONSTANTS
print_debugging = False  # whether to print debugging information
yaxis = "MICROSECONDS"  # can be SECONDS, MILLISECONDS, MINUTES or MICROSECONDS
exhaustive_color, dp_color = "red", "blue"  # matplotlib colors
num_tests = 20  # number of entries to test
input_dimensions = (5, 12)  # (min, max) dimensions of the input grids
seed = None  # random seed for reproducibility, set to None for random seed
# --------------------------------------------------------------------------------

# Set up program
s = datetime.now().microsecond * datetime.now().second if seed is None else seed
if print_debugging:
    print(f"Using seed {s}\n")
r.seed(s)


# Convert time to the designated time stamp
def convert_time(x: float) -> int:
    match yaxis:
        case "MINUTES":
            return x / 60
        case "SECONDS":
            return x
        case "MILISECONDS":
            return x * 1000
        case _:
            return x * 1000000


# Define the Solver object that contains methods to
# solve the problem in exhaustive and DP ways
solver = Solve()


# Create a random grid
def make_grid() -> list[str]:
    # Decide density/sparsity percent
    c = r.randint(5, 30)
    # Create dimensions r and c
    rows, cols = [r.randint(*input_dimensions) for _ in range(2)]
    # Instantiate a grid
    grid = [
        ["X" if r.randint(1, 100) <= c else "." for _ in range(cols)]
        for _ in range(rows)
    ]
    if print_debugging:
        print(f"Generated new grid size {rows}x{cols} with {c}% chance per X:")
        print("\n".join(" ".join(row) for row in grid))
    # Return the randomly generated grid
    return grid


# Helper function to print the grid
def print_grid(grid) -> None:
    for line in grid:
        print(line)
    print()


# Create a scatterplot given the results list, color, and label
def make_scatterplot(results: list[tuple[int, int]], color, label) -> None:
    # Make a plot with both data points
    plt.scatter(*zip(*results), color=color, label=label)
    plt.xlabel("Size")
    plt.ylabel(f"Time ({yaxis.title()})")
    plt.legend()
    plt.show()


# Run a test using the exhaustive algorithm
def run_exhaustive(grid: list[str]) -> tuple[int, int, int]:
    # Set the solver to use the new grid
    solver.set_field(grid)
    # Test the exhaustive solution
    start_e = time()
    res = solver.solve_exhaustive()
    end_e = time()
    rows, cols = len(grid), len(grid[0])
    return (res, rows + cols - 2, convert_time(end_e - start_e))


# Run a test using the dp algorithm
def run_dp(grid: list[str]) -> tuple[int, int, int]:
    solver.set_field(grid)
    # Test the dp solution
    start_d = time()
    res = solver.solve_dp()
    end_d = time()
    rows, cols = len(grid), len(grid[0])
    return (res, max(rows, cols), convert_time(end_d - start_d))


# Define a function to prompt the user on which file to test
# and call the file based on the users input
def main() -> None:
    print("This program will solve The Opponent Avoidance Problem with 2 methods")
    print("1. Exhaustive Search")
    print("2. Dynamic Programming\n")

    exhaustive_results, dp_results = [], []
    overall_results = []

    # Run the tests
    iter_obj = (
        range(num_tests)
        if print_debugging or not prog
        else tqdm(range(num_tests), desc="Testing")
    )
    for _ in iter_obj:
        grid = make_grid()
        e = run_exhaustive(grid)
        d = run_dp(grid)
        exhaustive_results.append((e[1], e[2]))
        dp_results.append((d[1], d[2]))

        e_res = f"Exhaustive Total Paths: {e[0]}"
        e_time = f"Exhaustive Empirical Time: {e[2]}"
        d_res = f"Dynamic Programming Total Paths: {d[0]}"
        d_time = f"Dynamic Programming Empirical Time: {d[2]}"

        overall_results.append(((e_res, e_time), (d_res, d_time), grid))

    # Comment the following section if you
    # wish to not see results in standard output

    for res in overall_results:
        print("Test case Input:")
        print_grid(res[2])
        print(res[0][0])
        print(res[0][1], "\n")
        print(res[1][0])
        print(res[1][1], "\n")

    make_scatterplot(exhaustive_results, exhaustive_color, "Exhaustive Approach")
    make_scatterplot(dp_results, dp_color, "Dynamic Programming Approach")


# If this is the main process, call the linker function to prompt the user
if __name__ == "__main__":
    main()
