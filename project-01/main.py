# Name: Tomas Oh
# CSUF Email: tomasoh@csu.fullerton.edu
# CWID: 885566877
# Submission is for Project 1 of CPSC 335-04

import greedy
import pairs


# Define a function to prompt the user on which file to test
# and call the file based on the users input
def linker() -> None:
    # Prompt the user
    print("Please enter a number for which file to test:\n")
    print("1. Connecting Pairs of Persons")
    print("2. Greedy Approach to Hamiltonian Problem\n")
    print("Enter anything else to exit\n")

    # Take user input
    response = input("Your input here: ").strip()
    print()

    # Match their input to a function to test
    match response:
        case "1":
            print("Running Problem #1: Connecting Pairs of Persons\n")
            pairs.execute()
        case "2":
            print("Running Algorithm #2: Greedy Approach to Hamiltonian Problem\n")
            greedy.execute()

    # Finishing statement before quitting the program
    print("Good Bye!")


# If this is the main process, call the linker function to prompt the user
if __name__ == "__main__":
    linker()
