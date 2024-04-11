# Name: Tomas Oh
# CSUF Email: tomasoh@csu.fullerton.edu
# CWID: 885566877
# Submission is for Project 3 of CPSC 335 (Section 04)

from solve import Solve

NUM_TESTS = 3


# Define a function to prompt the user on which file to test
# and call the file based on the users input
def linker() -> None:
    print("This program will solve The Opponent Avoidance Problem with 2 methods")
    # Prompt the user
    print("Please enter a number for which method implementation to test:\n")
    print("1. Exhaustive Search")
    print("2. Dynamic Programming\n")
    print("Enter anything else to exit\n")

    # Take user input
    response = input("Your input here: ").strip()
    print()

    if response in {"1", "2"}:
        method_name = "Exhaustive Search" if response == "1" else "Dynamic Programming"
        print(f"Running Algorithm #{response}: {method_name}\n")

        for i in range(NUM_TESTS):
            solve = Solve(i + 1)
            print(f"Input #{i + 1}:\n")
            solve.print_grid()

            output = solve.solve_exhaustive() if response == "1" else solve.solve_dp()
            print("Output:", output, "\n")

    print("Good Bye!")


# If this is the main process, call the linker function to prompt the user
if __name__ == "__main__":
    linker()
