from time import time
from parse import parse_list


def greedy_hamiltonian(distances: list[int], fuel: list[int], mpg: int) -> int:
    return -1


# Define the main process when this file is run
def main() -> None:
    # Prompt the user for the input for the function
    print(
        "Enter a list of integers, seperated by either spaces or commas, with or without brackets,"
    )
    print("This will be for the distances input:\n")
    response1 = input("Your input here: ")
    print()
    print(
        "Enter a list of integers, seperated by either spaces or commas, with or without brackets,"
    )
    print("this will be for the fuel input:\n")
    response2 = input("Your input here: ")
    print()
    print("Please enter the miles per gallon input:\n")
    response3 = input("Your input here: ").strip()
    print()
    # Parse the input into a list of integers before calling the function
    arg1 = parse_list(response1)
    arg2 = parse_list(response2)
    if not response3.isnumeric():
        print("Invalid input for miles per gallon.")
        return
    arg3 = int(response3)
    # Call the function and print the result
    print("Inputs:")
    print("distances =", arg1)
    print("fuel =", arg2)
    print("mpg =", arg3, "\n")
    print("Calling solution function...")
    start = time()
    print("Output: ", greedy_hamiltonian(arg1, arg2, arg3))
    end = time()
    print()
    print("Time taken:", (end - start) * 1000, "ms")
    return


if __name__ == "__main__":
    main()
