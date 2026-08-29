from HabitDatabase import HabitDatabase
from datetime import datetime
from Habit import Habit
from utilities import get_non_empty_input, get_periodicity_input, get_habit_number_input
import analytics

class HabitManager:
    def __init__(self):
        self.database = HabitDatabase()
        self.habit_list = self.database.get_all_habits();

    def add_new_habit(self):
        habit_name = get_non_empty_input("Habit name", "Enter a name for your new habit: ")
        habit_description = input("Enter a description for your new habit (optional): ").strip()
        habit_periodicity = get_periodicity_input("Enter the desired periodicity for your habit (daily/weekly): ")

        new_habit = Habit(None, habit_name, habit_description, habit_periodicity, datetime.now(), [])
        self.database.add_habit(new_habit)
        self.habit_list.append(new_habit)
        print("New habit added successfully.\n")

    def view_all_habits(self):
        print("\nHere is a list of all your habits (latest first): ")
        print(f"{analytics.view_all_habits(self.habit_list)}\n")

    def check_off_habit(self):
        self.view_all_habits()

        sorted_habits = sorted(self.habit_list, key = lambda habit: habit.created_at, reverse = True)
        habit_identifier = get_habit_number_input(1, len(sorted_habits))

        chosen_habit = sorted_habits[habit_identifier - 1]
        current_time = datetime.now()
        self.database.check_off_habit(chosen_habit.id, current_time)
        chosen_habit.check_off_habit(current_time)

        print(f"Habit #{habit_identifier} - '{chosen_habit.name}' was checked off at {current_time.isoformat()}.\n")