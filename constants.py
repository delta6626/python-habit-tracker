from typing import Literal

MENU_OPTIONS = {
    "add_habit": 1,
    "complete_habit": 2,
    "delete_habit": 3,
    "view_analytics": 4,
    "repeat_menu": 5,
    "exit": 6
}

MENU_OPTIONS_TEXT = f"""
Press {MENU_OPTIONS['add_habit']} to add a new habit
Press {MENU_OPTIONS['complete_habit']} to complete/check-off a habit
Press {MENU_OPTIONS['delete_habit']} to delete a habit
Press {MENU_OPTIONS['view_analytics']} to view analytics
Press {MENU_OPTIONS['repeat_menu']} to see the menu again
Press {MENU_OPTIONS['exit']} to exit
"""

ANALYTICS_OPTIONS = {
    "get_all_habits": 1,
    "get_habit_details": 2,
    "get_all_habits_with_same_periodicty": 3,
    "get_longest_streak_overall": 4,
    "get_longest_streak_for_habit": 5,
}

ANALYTICS_OPTIONS_TEXT = f"""
Press {ANALYTICS_OPTIONS['get_all_habits']} to view all habits
Press {ANALYTICS_OPTIONS['get_habit_details']} to view a habit in detail
Press {ANALYTICS_OPTIONS['get_all_habits_with_same_periodicty']} to view all habits with the same periodicity
Press {ANALYTICS_OPTIONS['get_longest_streak_overall']} to view the longest streak overall
Press {ANALYTICS_OPTIONS['get_longest_streak_for_habit']} to view the longest streak for a specific habit
"""

INVALID_INPUT_TEXT = f"""
Invalid option. Enter a valid one or press {MENU_OPTIONS['repeat_menu']} to view all valid options.
"""

INVALID_HABIT_IDENTIFIER = "Invalid identifier. Please enter a valid habit identifier."

VALUE_ERROR_MESSAGE = "Invalid input. Please enter a number."

Periodicity = Literal["daily", "weekly"]
PERIODICITY_DAY_COUNT:dict[Periodicity, int] = {
    "daily": 1,
    "weekly":7
}


MAIN_TABLE_NAME = "habits"
COMPLETIONS_TABLE_NAME = "completions"

GET_ALL_HABITS_SQL= f"""
SELECT * FROM {MAIN_TABLE_NAME}
"""

GET_HABIT_COMPLETIONS_SQL = f"""
SELECT completed_at
FROM {COMPLETIONS_TABLE_NAME}
WHERE habit_id = ?
"""

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