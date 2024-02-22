import greedy
import pairs


# Define a function to prompt the user on which file to test
# and call the fail based on the users input
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
            pairs.main()
        case "2":
            greedy.main()
        case _:
            print("Exiting...")
            return


# If this is the main process, call the linker function to prompt the user
if __name__ == "__main__":
    linker()
