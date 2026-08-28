from HabitDatabase import HabitDatabase
from Habit import Habit
from datetime import datetime

menu_options = {
    "add_habit": 1,
    "complete_habit": 2,
    "delete_habit": 3,
    "view_analytics": 4,
    "repeat_menu": 5,
    "exit": 6
}

menu_options_text = f"""
Press {menu_options['add_habit']} to add a new habit
Press {menu_options['complete_habit']} to complete/check-off a habit
Press {menu_options['delete_habit']} to delete a habit
Press {menu_options['view_analytics']} to view analytics
Press {menu_options['repeat_menu']} to see the menu again
Press {menu_options['exit']} to exit
"""

invalid_input_text = f"""
Invalid option. Enter a valid one or press {menu_options['repeat_menu']} to view all valid options.
"""

database = HabitDatabase()

def add_new_habit():
    habit_name = input("Enter a name for your new habit: ")

    if habit_name.strip() == "":
        print("Habit name cannot be empty.")
        return

    habit_description = input("Enter a description for your new habit (optional): ")

    habit_periodicity = input("Enter the desired periodicity for your habit (daily/weekly): ").strip().lower()

    if habit_periodicity == "":
        print("Periodicity cannot be empty.")
        return

    if habit_periodicity not in ("daily", "weekly"):
        print("Invalid periodicity.")
        return

    new_habit = Habit(habit_name, habit_description, habit_periodicity, datetime.now(), [])
    database.add_habit(new_habit)    

def main():
    """
    The main function serves as the entrypoint to the application.
    """

    print("Welcome to the habit tracker application")
    print(menu_options_text)

    while(True):
        try:
            chosen_option = int(input("Please enter your preferred option: "))

            if chosen_option == menu_options["add_habit"]:
                add_new_habit()
            elif chosen_option == menu_options["complete_habit"]:
                pass
            elif chosen_option == menu_options["delete_habit"]:
                pass
            elif chosen_option == menu_options["view_analytics"]:
                pass
            elif chosen_option == menu_options["repeat_menu"]:
                print(menu_options_text)
            elif chosen_option == menu_options["exit"]:
                print("Goodbye.")
                break
            else:
                print(invalid_input_text)
        except ValueError:
            print(invalid_input_text);


if __name__ == "__main__":
    main()