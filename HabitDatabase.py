import sqlite3
from datetime import datetime
from Habit import Habit

MAIN_TABLE_NAME = "habits"
COMPLETIONS_TABLE_NAME = "completions"

CREATE_HABITS_TABLE_SQL = f"""
CREATE TABLE IF NOT EXISTS {MAIN_TABLE_NAME} (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    periodicity TEXT NOT NULL,
    created_at TEXT NOT NULL
)
"""

CREATE_COMPLETIONS_TABLE_SQL = f"""
CREATE TABLE IF NOT EXISTS {COMPLETIONS_TABLE_NAME} (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    habit_id TEXT NOT NULL,
    completed_at TEXT NOT NULL,
    FOREIGN KEY (habit_id) REFERENCES {MAIN_TABLE_NAME}(id) ON DELETE CASCADE
)
"""

INSERT_HABIT_SQL = f"""
INSERT INTO {MAIN_TABLE_NAME} (
    id,
    name,
    description,
    periodicity,
    created_at
)
VALUES (?, ?, ?, ?, ?)
"""

CHECK_OFF_HABIT_SQL = f"""
INSERT INTO {COMPLETIONS_TABLE_NAME} (
    habit_id,
    completed_at
)
VALUES (?, ?)
"""

DELETE_HABIT_SQL = f"""
DELETE FROM {MAIN_TABLE_NAME}
WHERE id = ?
"""

class HabitDatabase:
    def __init__(self):
        self.connection = sqlite3.connect("habit_database.db")
        self.connection.execute("PRAGMA foreign_keys = ON")

        self.cursor = self.connection.cursor()
        self.cursor.execute(CREATE_HABITS_TABLE_SQL)
        self.cursor.execute(CREATE_COMPLETIONS_TABLE_SQL)

        self.connection.commit()

    def add_habit(self, habit: Habit)->None:
        self.cursor.execute(INSERT_HABIT_SQL, (habit.id, habit.name, habit.description, habit.periodicity, habit.created_at.isoformat()))
        self.connection.commit()

    def check_off_habit(self, habit_id:str):
        self.cursor.execute(CHECK_OFF_HABIT_SQL, (habit_id, datetime.now().isoformat()))
        self.connection.commit()

    def delete_habit(self, habit_id:str):
        self.cursor.execute(DELETE_HABIT_SQL, (habit_id,))
        self.connection.commit()