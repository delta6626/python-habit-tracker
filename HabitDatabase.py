import sqlite3
import constants
from datetime import datetime
from Habit import Habit


class HabitDatabase:
    def __init__(self):
        self.connection = sqlite3.connect("habit_database.db")
        self.connection.execute("PRAGMA foreign_keys = ON")

        self.cursor = self.connection.cursor()
        self.cursor.execute(constants.CREATE_HABITS_TABLE_SQL)
        self.cursor.execute(constants.CREATE_COMPLETIONS_TABLE_SQL)

        self.connection.commit()

    def get_all_habits(self):
        self.cursor.execute(constants.GET_ALL_HABITS_SQL);
        return self.cursor.fetchall();

    def add_habit(self, habit: Habit)->None:
        self.cursor.execute(constants.INSERT_HABIT_SQL, (habit.id, habit.name, habit.description, habit.periodicity, habit.created_at.isoformat()))
        self.connection.commit()

    def check_off_habit(self, habit_id:str):
        self.cursor.execute(constants.CHECK_OFF_HABIT_SQL, (habit_id, datetime.now().isoformat()))
        self.connection.commit()

    def delete_habit(self, habit_id:str):
        self.cursor.execute(constants.DELETE_HABIT_SQL, (habit_id,))
        self.connection.commit()