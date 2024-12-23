# daily_reminder.py

def daily_reminder():
    while True:
        # Prompt user for task details
        task = input("Enter your task: ").strip()
        priority = input("Priority (high/medium/low): ").strip().lower()
        time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

        # If-elif logic for priority level
        if priority == "high":
            base_message = f"'{task}' is a high priority task."
        elif priority == "medium":
            base_message = f"'{task}' is a medium priority task."
        elif priority == "low":
            base_message = f"'{task}' is a low priority task."
        else:
            print("Invalid priority level. Please enter high, medium, or low.")
            continue

        # Add time-sensitivity message
        if time_bound == "yes":
            reminder = f"{base_message} It requires immediate attention today!"
        elif time_bound == "no":
            reminder = f"{base_message} Consider completing it when you have free time."
        else:
            print("Invalid input for time-bound. Please enter yes or no.")
            continue

        # Print the reminder
        print(f"\nReminder: {reminder}\n")

        # Ask if the user wants to input another task
        another = input("Do you want to add another task? (yes/no): ").strip().lower()
        if another != "yes":
            print("\nThank you for using the Daily Reminder! Have a productive day!")
            break

if __name__ == "__main__":
    daily_reminder()
