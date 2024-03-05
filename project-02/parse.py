def parse_list(user_input: str) -> list[int]:
    output = []

    with open("sample2.txt", "r") as f:
        for line in f:
            line = line.replace("(", "").replace(")", "")
            line = [int(item) for item in line.split(",")]
            output.append(line)
    return output
