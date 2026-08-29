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

    def get_all_habits(self) -> list[Habit]:
        self.cursor.execute(constants.GET_ALL_HABITS_SQL)
        habits = self.cursor.fetchall()
        habit_objects = []

        for habit in habits:
            habit_id, name, description, periodicity, created_at = habit
            self.cursor.execute(constants.GET_HABIT_COMPLETIONS_SQL, (habit_id,))
            completion_rows = self.cursor.fetchall()

            completions = []
            for row in completion_rows:
                completion = datetime.fromisoformat(row[0])
                completions.append(completion)

            existing_habit = Habit(
                habit_id,
                name,
                description,
                periodicity,
                datetime.fromisoformat(created_at),
                completions
            )

            habit_objects.append(existing_habit)

        return habit_objects

    def add_habit(self, habit: Habit) -> None:
        self.cursor.execute(constants.INSERT_HABIT_SQL, (habit.id, habit.name, habit.description, habit.periodicity, habit.created_at.isoformat()))
        self.connection.commit()

    def check_off_habit(self, habit_id:str, check_off_datetime:datetime) -> None:
        self.cursor.execute(constants.CHECK_OFF_HABIT_SQL, (habit_id, check_off_datetime.isoformat()))
        self.connection.commit()

    def delete_habit(self, habit_id:str) -> None:
        self.cursor.execute(constants.DELETE_HABIT_SQL, (habit_id,))
        self.connection.commit()