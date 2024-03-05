from parse import parse_list


def largest_sum(nums: list[int]):
    return -1


# Define the main execution process when this file is run
def execute() -> None:
    # Process all the sample inputs (vector - list of integers) for each test
    # case, outputting the result of calling the function largest_sum()
    for i, sample_input in enumerate(parse_list()):
        print(f"Test Case #{i + 1}\n")

        print("Input:\n")
        print("Vector v = ", sample_input)

        print("Output: ", largest_sum(sample_input), "\n\n")
