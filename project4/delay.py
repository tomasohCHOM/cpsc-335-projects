# Name: Tomas Oh
# CSUF Email: tomasoh@csu.fullerton.edu
# CWID: 885566877
# Submission is for Project 4 of CPSC 335 (Section 04)


# sample_inputs is a list that contains all the inputs for each test case.
# If you wish to run more test cases against the algorithm, you may modify
# this variable by adding another entry to the list, similar to the one
# provided. Note that it has to contain the "times," "n," and "k" keys with
# their corresponding values as per the problem statement.
sample_inputs = [
    {"times": [2, 1, 1], "n": 4, "k": 2},
    {"times": [1, 2, 1], "n": 2, "k": 2},
    {"times": [1, 2, 1], "n": 2, "k": 2},
]


def min_time(times: list[list[int]], n: int, k: int) -> int:
    return 0


# Define the main execution process when this file is run
def execute() -> None:
    # Process all the sample inputs (times - list of integers,
    # n - a single integer, and k - a single integer) for each
    # test case, outputting the result of calling the function
    # min_time()
    for i, input in enumerate(sample_inputs):
        print(f"Test Case #{i + 1}\n")
        times = input["times"]
        n = input["n"]
        k = input["k"]

        print("Inputs:\n")
        print("times = ", times)
        print("n = ", n)
        print("k = ", k, "\n")

        print("Output:", min_time(times, n, k), "\n\n")
