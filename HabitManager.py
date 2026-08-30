from HabitDatabase import HabitDatabase
from datetime import datetime
from Habit import Habit
from utilities import get_non_empty_input, get_periodicity_input, get_habit_number_input
import analytics

class HabitManager:
    def __init__(self):
        self.database = HabitDatabase()
        self.habit_list = self.database.get_all_habits();

    def initiate_add_new_habit(self) -> None:
        habit_name = get_non_empty_input("Habit name", "Enter a name for your new habit: ")
        habit_description = input("Enter a description for your new habit (optional): ").strip()
        habit_periodicity = get_periodicity_input("Enter the desired periodicity for your habit (daily/weekly): ")

        new_habit = Habit(None, habit_name, habit_description, habit_periodicity, datetime.now(), [])
        self.database.add_habit(new_habit)
        self.habit_list.append(new_habit)
        print("New habit added successfully.\n")

    def initiate_view_all_habits(self) -> None:
        print("\nHere is a list of all your habits (latest first): ")
        print(f"{analytics.view_all_habits(self.habit_list)}\n")

    def initiate_check_off_habit(self) -> None:
        self.initiate_view_all_habits()

        sorted_habits = sorted(self.habit_list, key = lambda habit: habit.created_at)
        habit_identifier = get_habit_number_input("Enter the identifier of the habit you would like to check off: ", 1, len(sorted_habits))

        chosen_habit = sorted_habits[habit_identifier - 1]
        current_time = datetime.now()
        self.database.check_off_habit(chosen_habit.id, current_time)
        chosen_habit.check_off_habit(current_time)

        print(f"Habit #{habit_identifier} - '{chosen_habit.name}' was checked off at {current_time.isoformat()}.\n")

    def initiate_delete_habit(self) -> None:
        self.initiate_view_all_habits()
        
        sorted_habits = sorted(self.habit_list, key = lambda habit: habit.created_at)
        habit_identifier = get_habit_number_input("Enter the identifier of the habit you would like to delete: ", 1, len(sorted_habits))

        chosen_habit = sorted_habits[habit_identifier - 1]
        self.database.delete_habit(chosen_habit.id)
        self.habit_list.remove(chosen_habit)

        print(f"Habit #{habit_identifier} - '{chosen_habit.name}' was deleted successfully.\n")