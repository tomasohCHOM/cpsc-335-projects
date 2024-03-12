# sample_inputs is a list that contains all the inputs for each test case.
# If you wish to run more test cases against the algorithm, you may modify
# this variable by adding another entry in the list (separated by a comma).
# Any new inputs must be valid test cases against the algorithm (please take
# a look at the first sample input and the comments to see what the algorithm's
# input looks like).
sample_inputs = [
    {
        # Represents the time intervals when person 1 is occupied
        "person1_schedule": [["7:00", "8:30"], ["12:00", "13:00"], ["16:00", "18:00"]],
        # Represents the starting and end time of person 1's daily active times
        "person1_daily": ["9:00", "19:00"],
        # Represents the time intervals when person 2 is occupied
        "person2_schedule": [
            ["9:00", "10:30"],
            ["12:20", "13:30"],
            ["14:00", "15:00"],
            ["16:00", "17:00"],
        ],
        # Represents the starting and end time of person 2's daily active times
        "person2_daily": ["9:00", "18:30"],
        # Represents the time (in minutes) that the scheduled meeting
        # would last for
        "duration": 30,
    }
]


def available_schedules(
    person1_schedule: list[list[str]],
    person1_daily: list[list[str]],
    person2_schedule: list[list[str]],
    person2_daily: list[list[str]],
    duration: int,
) -> list[list[str]]:
    # Initialize two pointers p1 = p2 = 0
    p1 = p2 = 0
    # Initialize unavailabilities to an empty array. This will hold
    # ALL the times when either person1 or person2 is unavailable
    unavailabilities = []
    while p1 < len(person1_schedule) and p2 < len(person2_schedule):
        p1 += 1
        p2 += 1
    return []


# Define the main execution process when this file is run
def execute() -> None:
    for i, input in enumerate(sample_inputs):
        print(f"Test Case #{i + 1}\n")
        person1_schedule = input["person1_schedule"]
        person1_daily = input["person1_availability"]
        person2_schedule = input["person2_schedule"]
        person2_daily = input["person2_availability"]
        duration = input["duration"]

        print("Input:\n")
        print("Person 1 Schedule =", person1_schedule, "\n")
        print("Person 1 Availability =", person1_daily, "\n")
        print("Person 2 Schedule =", person2_schedule, "\n")
        print("Person 2 Availability =", person2_daily, "\n")
        print("Meeting Duration =", duration, "\n")

        print(
            "Output: ",
            available_schedules(
                person1_schedule,
                person1_daily,
                person2_schedule,
                person2_daily,
                duration,
            ),
            "\n\n",
        )
