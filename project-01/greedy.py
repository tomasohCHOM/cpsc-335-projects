from time import time
from parse import parse_list

sample_input = {"distances": [5, 25, 15, 10, 15], "fuel": [1, 2, 1, 0, 3], "mpg": 10}


def greedy_hamiltonian(distances: list[int], fuel: list[int], mpg: int) -> int:
    # Initialize surplus to 0. This will indicate how
    # much gas is left in our tank to travel around cities
    surplus = 0
    # Initialize start to 0. This will be our returning value
    start = 0

    # Loop through distances array, keeping track of index
    for i in range(len(distances)):
        # Update global_max and local_max
        surplus += fuel[i] * mpg - distances[i]

        # If surplus is less than 0, we know we cannot
        # reach our destination from our starting point
        # because we will not have enough gas. Instead, start
        # from the city next to it (i + 1). We do not worry about
        # circling around (starting at city with index = 0) because
        # we already looped through it
        if surplus < 0:
            surplus = 0
            start = i + 1

    # return the starting index of the preferred starting city
    return start


# Define the main process when this file is run
def main() -> None:
    distances = sample_input["distances"]
    fuel = sample_input["fuel"]
    mpg = sample_input["mpg"]

    print("\nInputs:")
    print("distances = ", distances)
    print("fuel = ", fuel)
    print("mpg = ", mpg, "\n")
    print("Calling solution function...\n")

    print("Output: ", greedy_hamiltonian(distances, fuel, mpg), "\n")


if __name__ == "__main__":
    main()
