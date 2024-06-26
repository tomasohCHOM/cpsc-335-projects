# Name: Tomas Oh
# CSUF Email: tomasoh@csu.fullerton.edu
# CWID: 885566877
# Submission is for Project 2 of CPSC 335 (Section 04)

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
    p1_schedule: list[list[str]],
    p1_daily: list[str],
    p2_schedule: list[list[str]],
    p2_daily: list[str],
    duration: int,
) -> list[list[str]]:
    # Initialize two pointers p1 = p2 = 0
    p1 = p2 = 0
    # Initialize unavailabilities to a list. This will hold
    # ALL the times when either person1 or person2 is unavailable

    # Append the first interval which considers the lower bound
    unavailabilities = [["00:00", max(p1_daily[0], p2_daily[0])]]

    # Get each of the unavailable intervals in our list,
    # ensuring that we have them sorted for convenience
    while p1 < len(p1_schedule) or p2 < len(p2_schedule):
        if p1 == len(p1_schedule):
            unavailabilities.append(p2_schedule[p2])
            p2 += 1
            continue
        if p2 == len(p2_schedule):
            unavailabilities.append(p1_schedule[p1])
            p1 += 1
            continue
        if compare_times(p1_schedule[p1][0], p2_schedule[p2][0]) == -1:
            unavailabilities.append(p1_schedule[p1])
            p1 += 1
        else:
            unavailabilities.append(p2_schedule[p2])
            p2 += 1

    # Append the last interval which considers the upper bound
    unavailabilities.append([min(p1_daily[1], p2_daily[1]), "24:00"])

    # Merge the times that are overlapping into single intervals
    merged = [unavailabilities[0]]
    for time in unavailabilities:
        # Compare the current end time to the next start time
        end1, start2 = merged[-1][1], time[0]
        if compare_times(end1, start2) == -1:
            # If end1 < start2, append that time to merged
            merged.append(time)
        else:
            # Else, modify the second entry in the last element of
            # merged to contain the max(end1, time[1])
            merged[-1][1] = end1 if compare_times(end1, time[1]) == 1 else time[1]

    output = []
    # Loop through the merged intervals and find the available times
    for i in range(1, len(merged)):
        end1, start2 = merged[i - 1][1], merged[i][0]
        # If the interval located at either of the bounds, we can schedule
        # meeting if its is greater or exactly the specified duration
        if i == 1 or i == len(merged) - 1:
            if time_to_minutes(start2) - time_to_minutes(end1) >= duration:
                output.append([end1, start2])

        # It will be an available time if start2 - end1 > duration of
        # meeting (30 minutes, for example)
        elif time_to_minutes(start2) - time_to_minutes(end1) > duration:
            output.append([end1, start2])

    return output


# Helper function that compares time1 and time2, returning 1
# if time1 > time2, 0 if time1 == time2, or -1 if time1 < time2
def compare_times(time1: str, time2: str):
    converted_time1 = time_to_minutes(time1)
    converted_time2 = time_to_minutes(time2)

    if converted_time1 > converted_time2:
        return 1
    if converted_time1 == converted_time2:
        return 0
    if converted_time1 < converted_time2:
        return -1


# Converts a string in military time format to minutes (int)
def time_to_minutes(time):
    hr, min = time.split(":")
    return int(hr) * 60 + int(min)


# Converts an integer "minutes" to military time format
def minutes_to_time(minutes):
    return f"{minutes//60}:{minutes%60:02d}"


# Define the main execution process when this file is run
def execute() -> None:
    for i, input in enumerate(sample_inputs):
        print(f"Test Case #{i + 1}\n")
        person1_schedule = input["person1_schedule"]
        person1_daily = input["person1_daily"]
        person2_schedule = input["person2_schedule"]
        person2_daily = input["person2_daily"]
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
