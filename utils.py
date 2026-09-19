import json
from datetime import datetime, timedelta
from sqlite3 import Cursor
import constants
from Habit import Habit

config_file_name = "config.json"


def is_demo_data_loaded() -> bool:
    try:
        with open(config_file_name, "r") as file:
            config_data = json.load(file)
            return config_data["demo_data_loaded"]

    except (FileNotFoundError, KeyError):
        config_data = {"demo_data_loaded": False}

        with open(config_file_name, "w") as file:
            json.dump(config_data, file)

        return False


def update_demo_data_status(status: bool) -> None:
    try:
        with open(config_file_name, "r") as file:
            config_data = json.load(file)

        config_data["demo_data_loaded"] = status

        with open(config_file_name, "w") as file:
            json.dump(config_data, file)

    except (FileNotFoundError, KeyError):
        config_data = {"demo_data_loaded": status}

        with open(config_file_name, "w") as file:
            json.dump(config_data, file)


def build_demo_habits(now: datetime | None = None) -> list[Habit]:
    now = now or datetime.now()

    def offset_time(days_ago: int, hour: int, minute: int) -> datetime:
        return (now - timedelta(days=days_ago)).replace(
            hour=hour, minute=minute, second=0, microsecond=0
        )

    habits = []

    # 1. Daily habit with a 28 day perfect streak
    created = offset_time(28, 8, 0)
    completions = [offset_time(d, 8, 0) for d in range(27, -1, -1)]
    habits.append(
        Habit(
            "TDR1",
            "Drink water",
            "Drink 2 liters of water everyday",
            "daily",
            created,
            completions,
        )
    )

    # 2. Daily habit with a broken streak. 3 days gap. Day 11, 12 and 13.
    created = offset_time(28, 7, 30)
    completions = [
        offset_time(d, 7, 30) for d in range(27, -1, -1) if not (11 <= d <= 13)
    ]
    habits.append(
        Habit(
            "TDR2",
            "Daily run",
            "Run for 2 kilometers everyday ",
            "daily",
            created,
            completions,
        )
    )

    # 3. Daily habit with a single missed day (day 5).
    created = offset_time(28, 21, 0)
    completions = [offset_time(d, 21, 0) for d in range(27, -1, -1) if d != 5]
    habits.append(
        Habit(
            "TDR3",
            "Daily meditation",
            "Meditate for 30 minutes everyday",
            "daily",
            created,
            completions,
        )
    )

    # 4. Weekly habit with a perfect 4-week streak
    created = offset_time(28, 10, 0)
    completions = [offset_time(d, 10, 0) for d in (28, 21, 14, 7)]
    habits.append(
        Habit(
            "TDR4",
            "Read a book",
            "Read any book for half an hour or more",
            "weekly",
            created,
            completions,
        )
    )

    # 5. Weekly habit. Streak broken once in day 21.
    created = offset_time(28, 18, 0)
    completions = [offset_time(d, 18, 0) for d in (28, 14, 7)]
    habits.append(
        Habit(
            "TDR5",
            "Learn CS",
            "Learn a new CS concept every week",
            "weekly",
            created,
            completions,
        )
    )

    return habits


def seed_demo_data(cursor: Cursor, now: datetime | None = None) -> None:
    for habit in build_demo_habits(now):
        cursor.execute(
            constants.INSERT_HABIT_SQL,
            (
                habit.id,
                habit.name,
                habit.description,
                habit.periodicity,
                habit.created_at.isoformat(),
            ),
        )
        for completion in habit.completions:
            cursor.execute(
                constants.CHECK_OFF_HABIT_SQL, (habit.id, completion.isoformat())
            )
