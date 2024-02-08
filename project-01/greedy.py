from time import time
from re import sub


def greedy_hamiltonian(distances: list[int], fuel: list[int], mpg: int) -> int:
    return -1


# Define how to parse an input
def parse_list(user_input: str) -> list[int]:
    # Remove the square brackets if there are any
    user_input = user_input.replace("[", "").replace("]", "")
    # Replace commas with spaces then remove any leading/trailing whitespace
    user_input = user_input.replace(",", " ")
    user_input = user_input.strip()
    # Convert the input into a comma seperated int list for easy parsing
    user_input = sub(r"  *", ",", user_input)
    # Finally use list comprehension to convert the string into a list of integers
    return [int(x) for x in user_input.split(",")]


# Define the main process when this file is run
def main() -> None:
    # Prompt the user for the input for the function
    print(
        "Enter a list of integers, seperated by either spaces or commas, with or without brackets,"
    )
    print("this will be for the distances input:")
    print()
    response1 = input("~> ")
    print()
    print(
        "Enter a list of integers, seperated by either spaces or commas, with or without brackets,"
    )
    print("this will be for the fuel input:")
    print()
    response2 = input("~> ")
    print()
    print("Please enter the miles per gallon input:")
    print()
    response3 = input("~> ").strip()
    print()
    # Parse the input into a list of integers before calling the function
    arg1 = parse_list(response1)
    arg2 = parse_list(response2)
    if not response3.isnumeric():
        print("Invalid input for miles per gallon.")
        return
    arg3 = int(response3)
    # Call the function and print the result
    print("Calling solution function...")
    print()
    print("Inputs:")
    print("distances -", arg1)
    print("fuel -", arg2)
    print("mpg -", arg3)
    print()
    start = time()
    print("Output: ", greedy_hamiltonian(arg1, arg2, arg3))
    end = time()
    print()
    print("Time taken:", (end - start) * 1000, "ms")
    return


if __name__ == "__main__":
    main()
