from re import sub


# Define how to parse an input
def parse_list(user_input: str) -> list[int]:
    # Remove the square brackets if there are any
    user_input = user_input.replace("[", "").replace("]", "")
    # Replace commas with spaces then remove any leading/trailing whitespace
    user_input = user_input.replace(",", " ")
    user_input = user_input.strip()
    # Convert the input into a comma seperated int list for easy parsing
    user_input = sub(r"  *", ",", user_input)
    # Finally use list comprehension to convert the string into a list of integers
    return [int(x) for x in user_input.split(",")]
