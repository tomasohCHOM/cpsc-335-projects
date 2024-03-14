# Name: Tomas Oh
# CSUF Email: tomasoh@csu.fullerton.edu
# CWID: 885566877
# Submission is for Project 2 of CPSC 335 (Section 04)


# A helper function to parse txt file entries to a list
# of numbers (needed for Algorithm 2 - Arraylists and Subsets)
def parse_list(user_input: str) -> list[int]:
    output = []

    with open(user_input, "r") as f:
        for line in f:
            line = line.replace("(", "").replace(")", "")
            line = [int(item) for item in line.split(",")]
            output.append(line)
    return output


def largest_sum(nums: list[int]) -> tuple[int, int]:
    # Initialize variables beginning = 0 and end = 1
    beginning, end = 0, 1
    # Initialize max_sum to the lowest number possible
    max_sum = float("-inf")

    # Loop through each index i in the nums list
    for i in range(len(nums)):
        # Initialize a local_sum variable to 0
        local_sum = 0
        # Loop through each index j from i + 1 to end of list
        for j in range(i, len(nums)):
            # Add the current number at j to local_sum
            local_sum += nums[j]
            # If our local sum is greater than the maximum,
            # update beginning to i, end to j, and max_sum to
            # local_sum
            if local_sum > max_sum:
                beginning, end = i, j
                max_sum = local_sum

    # Return a sublist of the beginning and end indices of
    # the largest sum subarray in the nums list
    return nums[beginning : end + 1]


# Define the main execution process when this file is run
def execute() -> None:
    # Process all the sample inputs (vector - list of integers) for each test
    # case, outputting the result of calling the function largest_sum()
    for i, sample_input in enumerate(parse_list("sample2.txt")):
        print(f"Test Case #{i + 1}\n")

        print("Input:\n")
        print("Vector v = ", sample_input)

        print("Output: ", largest_sum(sample_input), "\n\n")
