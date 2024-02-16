from time import time
from parse import parse_list


def connect_pairs(row: list[int]) -> int:
    # Store the number of swaps for our answer
    swaps = 0
    # Map every number to its index
    indices = {person: i for i, person in enumerate(row)}
    # Now loop through our row
    for i in range(len(row)):
        # Store the person we're looking at
        person = row[i]
        # Figure out the partner for the person we're looking at
        partner = 0
        # If the current person is even, their partner is person + 1.
        # We will only match pairs when the current person is odd, to
        # avoid matching the same pair twice
        if person % 2 == 0:
            continue
        # If we are here, we know the partner is person - 1
        partner = person - 1
        # Let i and j be the current person and partners indices respectively
        j = indices[partner]
        # If the differene between i and j is greater than 1, they aren't
        # next to each other, and we need to swap
        if abs(i - j) > 1:
            # Use a temp variable for easy swapping
            temp = 0
            # First, swap them in the rows
            temp = row[j]
            row[j] = row[i + 1]
            row[i + 1] = temp
            # Next, swap the indices in our map
            temp = indices[row[j]]
            indices[row[j]] = indices[row[i + 1]]
            indices[row[i + 1]] = temp
            # Increase the number of swaps and move on to the next pairs
            swaps += 1
    # Return the number of swaps we made
    return swaps


def main() -> None:
    # Prompt the user for the input for the function
    print(
        "Please enter a list of integers seperated by either spaces or commas, with or without square brackets:\n"
    )
    response = input("Your input here: ")
    arg1 = parse_list(response)

    print("Calling solution function...\n")
    print("Input: ", arg1, "\n")

    start = time()
    print("Output: ", connect_pairs(row=arg1), print())
    end = time()

    print("Time taken:", (end - start) * 1000, "ms")


if __name__ == "__main__":
    main()
