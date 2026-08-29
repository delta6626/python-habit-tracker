from HabitDatabase import HabitDatabase
from datetime import datetime
from Habit import Habit
from utilities import get_non_empty_input, get_periodicity_input


class HabitManager:
    def __init__(self):
        self.database = HabitDatabase()

    def add_new_habit(self):
        habit_name = get_non_empty_input("Habit name", "Enter a name for your new habit: ")
        habit_description = input("Enter a description for your new habit (optional): ").strip()
        habit_periodicity = get_periodicity_input("Enter the desired periodicity for your habit (daily/weekly): ")

        new_habit = Habit(habit_name, habit_description, habit_periodicity, datetime.now(), [])
        self.database.add_habit(new_habit)