task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += ". Consider completing it when you have free time."
    
    case "medium":
        reminder = f"'{task}' is a medium priority task"
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += ". Consider completing it when you have free time."
    
    case "low":
        reminder = f"'{task}' is a low priority task"
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += ". Consider completing it when you have free time."
    
    case _:
        reminder = f"'{task}' has an unrecognized priority level"
        if time_bound == "yes":
            reminder += " but requires immediate attention today!"
        else:
            reminder += ". Consider reviewing the priority level."

print("Reminder:")
print(reminder)