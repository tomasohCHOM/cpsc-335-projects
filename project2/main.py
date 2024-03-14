# Name: Tomas Oh
# CSUF Email: tomasoh@csu.fullerton.edu
# CWID: 885566877
# Submission is for Project 2 of CPSC 335 (Section 04)

import schedules
import subsets


# Define a function to prompt the user on which file to test
# and call the file based on the users input
def linker() -> None:
    # Prompt the user
    print("Please enter a number for which file to test:\n")
    print("1. Ensuring Convenient Schedules")
    print("2. Arraylists and Subsets\n")
    print("Enter anything else to exit\n")

    # Take user input
    response = input("Your input here: ").strip()
    print()

    # Match their input to a function to test
    match response:
        case "1":
            print("Running Problem #1: Ensuring Convenient Schedules\n")
            schedules.execute()
        case "2":
            print("Running Algorithm #2: Arraylists and Subsets\n")
            subsets.execute()

    # Finishing statement before quitting the program
    print("Good Bye!")


# If this is the main process, call the linker function to prompt the user
if __name__ == "__main__":
    linker()
