from time import time
from parse import parse_list


def connect_pairs(row: list[int]) -> int:
    # Store the number of swaps for our answer
    swaps = 0
    # Map every number to its index
    indices = {person: i for (i, person) in enumerate(row)}

    # Loop through our row, by indices
    for i in range(len(row)):
        # Store the person we are currently looking at
        person = row[i]

        # Find the y partner of person as follows:
        # If the person's ID is even, we know that its partner's
        # ID is
        partner = person + 1 if person % 2 == 0 else person - 1
        # i and j are indices of the current person and its partner
        j = indices[partner]

        # If the difference between their indices is greater than 1,
        # we need to perform a swap since they are not next to each other
        if abs(i - j) > 1:
            # Swap the two people in the rows list
            row[i + 1], row[j] = row[j], row[i + 1]
            # Update the indices hash map values to match their new indices
            indices[row[i + 1]] = i + 1
            indices[row[j]] = j
            # Increase the number of swaps and move on to the next pairs
            swaps += 1
    # Return the output, which is the minimum number of swaps
    # such that the couples are all sitting next to each other
    return swaps


def main() -> None:
    # Prompt for user input (a list of integers)
    print(
        "Enter a list of integers, seperated by either spaces or commas, with or without brackets."
    )
    response1 = input("Your input here: ")

    try:
        arg1 = parse_list(response1)
    except:
        print("\nInvalid input for rows.\n")

    print("\nInput: ")
    print("rows =", arg1, "\n")

    print("Calling solution function...\n")
    start = time()
    print("Output: ", connect_pairs(row=arg1), "\n")
    end = time()

    print("Time taken:", (end - start) * 1000, "ms\n")


if __name__ == "__main__":
    main()
