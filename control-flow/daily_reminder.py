# daily_reminder.py

# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize reminder as empty
reminder = ""

# Process the task based on priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"Reminder: '{task}' has an unknown priority"

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
elif priority == "low" and time_bound == "no":
    reminder += ". Consider completing it when you have free time."

# --- ✅ CHECKS ---
# 1. Check if reminder message is generated
if not reminder:
    print("Error: No reminder could be generated. Please check your inputs.")
else:
    # 2. Check if reminder includes both priority and time sensitivity where needed
    if "priority" in reminder or "low priority" in reminder or "unknown" in reminder:
        print(reminder)
    else:
        print("Error: Reminder does not include priority information.")
