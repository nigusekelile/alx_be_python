# daily_reminder.py

# Prompt user for task details
task = input("Enter your task: ")
priority = input("Enter the priority (high/medium/low): ").lower()
time_bound = input("Is the task time-bound? (yes/no): ").lower()

# Process the task using match-case for priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a HIGH priority task."
    case "medium":
        reminder = f"Reminder: '{task}' is a MEDIUM priority task."
    case "low":
        reminder = f"Reminder: '{task}' is a LOW priority task."
    case _:
        reminder = f"Reminder: '{task}' has an UNKNOWN priority."

# Modify reminder if the task is time-bound
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"

# Display final reminder
print(reminder)
