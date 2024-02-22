# Name: Tomas Oh
# CSUF Email: tomasoh@csu.fullerton.edu
# CWID: 885566877
# Submission is for Project 1 of CPSC 335-04

# sample_inputs is a list that contains all the inputs for each test case.
# If you wish to run more test cases against the algorithm, you may modify
# this variable by adding another entry in the list (separated by a comma).
# It must be a valid test case, with the "row" as the key, and the value as
# the corresponding value of "row" (a list of integers), as per the problem
# statement.
sample_inputs = [{"row": [0, 2, 1, 3]}, {"row": [3, 2, 0, 1]}]


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


# Define the main execution process when this file is run
def execute() -> None:
    # Process all the sample inputs (rows - list of integers) for each test
    # case, outputting the result of calling the function connect_pairs()
    for i, input in enumerate(sample_inputs):
        print(f"Test Case #{i + 1}\n")
        row = input["row"]
        print("Input:\n")
        print("row =", row, "\n")

        print("Output: ", connect_pairs(row), "\n\n")
