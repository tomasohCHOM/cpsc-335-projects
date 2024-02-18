from time import time
from parse import parse_list


def greedy_hamiltonian(distances: list[int], fuel: list[int], mpg: int) -> int:
    return -1


# Define the main process when this file is run
def main() -> None:
    # Prompt for user input:
    #  distances - a list of integers
    #  fuel - a list of integers
    #  miles per gallon - an integer
    print(
        "\nEnter a list of integers, seperated by either spaces or commas, with or without brackets."
    )
    print("This will be for the distances input.")
    response1 = input("Your input here: ")

    print(
        "\nEnter a list of integers, seperated by either spaces or commas, with or without brackets."
    )
    print("This will be for the fuel input.")
    response2 = input("Your input here: ")

    try:
        arg1 = parse_list(response1)
        arg2 = parse_list(response2)
    except:
        print("\nInvalid input for either distances or fuel.\n")
        return

    print("\nEnter an integer, this will be the miles per gallon input.")
    response3 = input("Your input here: ").strip()

    if not response3.isnumeric():
        print("\nInvalid input for miles per gallon.\n")
        return
    arg3 = int(response3)

    print("\nInputs:")
    print("distances =", arg1)
    print("fuel =", arg2)
    print("mpg =", arg3, "\n")
    print("Calling solution function...\n")

    start = time()
    print("Output: ", greedy_hamiltonian(arg1, arg2, arg3), "\n")
    end = time()

    print("Time taken:", (end - start) * 1000, "ms")
    return


if __name__ == "__main__":
    main()
