# Name: Tomas Oh
# CSUF Email: tomasoh@csu.fullerton.edu
# CWID: 885566877
# Submission is for Project 4 of CPSC 335 (Section 04)

# sample_inputs is a list that contains all the inputs for each test case.
# If you wish to run more test cases against the algorithm, you may modify
# this variable by adding another entry in the list (separated by a comma).
# It must be a valid test case, with "start_end" as the key, and the value
# as the corresponding value of "start_end" (a list of [int, int]), as per
# the problem statement.
sample_inputs = [
    {
        "start_end": [
            [0, 2],
            [1, 4],
            [4, 6],
            [0, 4],
            [7, 8],
            [9, 11],
            [3, 10],
        ]
    }
]


def min_laptops(start_end: list[list[int, int]]) -> int:
    return 0


# Define the main execution process when this file is run
def execute() -> None:
    # Process all the sample inputs (start_end - list of list of of
    # integers) for each test case, outputting the result of calling
    # the function min_laptops()
    for i, input in enumerate(sample_inputs):
        print(f"Test Case #{i + 1}\n")
        start_end = input["start_end"]
        print("Input:\n")
        print("start_end =", start_end, "\n")

        print("Output:", min_laptops(start_end), "\n\n")
