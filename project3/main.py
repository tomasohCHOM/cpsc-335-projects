# Name: Tomas Oh
# CSUF Email: tomasoh@csu.fullerton.edu
# CWID: 885566877
# Submission is for Project 3 of CPSC 335 (Section 04)

from solve import Solve


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

    solve = Solve()
    print("Input:\n")
    solve.print_grid()

    # Match their input to a function to test
    match response:
        case "1":
            print("Running Algorithm #1: Exhaustive Search\n")
            print("Output:", solve.solve_exhaustive(), "\n")
        case "2":
            print("Running Algorithm #2: Dynamic Programming\n")
            print("Output:", solve.solve_dp(), "\n")

    # Finishing statement before quitting the program
    print("Good Bye!")


# If this is the main process, call the linker function to prompt the user
if __name__ == "__main__":
    linker()
