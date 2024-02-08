from time import time
from re import sub


def connect_pairs(row: list[int]) -> int:
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
        "Please enter a list of integers seperated by either spaces or commas, with or without square brackets:"
    )
    print()
    response = input("~> ")
    print()
    # Parse the input into a list of integers before calling the function
    arg1 = parse_list(response)
    # Call the function and print the result
    print("Calling solution function...")
    print()
    print("Input: ", arg1)
    print()
    start = time()
    print("Output: ", connect_pairs(arg1))
    end = time()
    print()
    print("Time taken:", (end - start) * 1000, "ms")
    return


if __name__ == "__main__":
    main()
