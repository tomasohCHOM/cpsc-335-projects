# Names: Brandon Dominguez, Sean Le, Tomas Oh, Gerrit Vanderstoel
# CSUF Emails: dominguezbrandon@csu.fullerton.edu, sdle@csu.fullerton.edu,
# tomasoh@csu.fullerton.edu, gvanderstoel29@csu.fullerton.edu
# CWIDs (in order of the names): 885691675, 886511047, 885566877, 886517630
# Submission is for Project 1 of CPSC 335 (Section 04)

# sample_inputs is a list that contains all the inputs for each test case.
# If you wish to run more test cases against the algorithm, you may modify
# this variable by adding another entry to the list, similar to the one
# provided. Note that it has to contain the "distances," "fuel," and "mpg"
# keys with their corresponding values as per the problem statement.
sample_inputs = [{"distances": [5, 25, 15, 10, 15], "fuel": [1, 2, 1, 0, 3], "mpg": 10}]


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


# Define the main execution process when this file is run
def execute() -> None:
    # Process all the sample inputs (distances - list of integers
    # fuel - list of integers, and mpg - a single integer) for each
    # test case, outputting the result of calling the function
    # greedy_hamiltonian()
    for i, input in enumerate(sample_inputs):
        print(f"Test Case #{i + 1}\n")
        distances = input["distances"]
        fuel = input["fuel"]
        mpg = input["mpg"]

        print("Inputs:\n")
        print("distances = ", distances)
        print("fuel = ", fuel)
        print("mpg = ", mpg, "\n")

        print("Output: ", greedy_hamiltonian(distances, fuel, mpg), "\n\n")
