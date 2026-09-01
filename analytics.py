from Habit import Habit
from datetime import datetime, timedelta
from constants import PERIODICITY_DAY_COUNT


def get_all_habits(habits: list[Habit]) -> str:
    return "\n".join(
        map(lambda item: f"{item[0]}. {item[1].name}", enumerate(habits, start=1))
    )


def get_habit_details(habit: Habit) -> str:
    completion_times = (
        "\n".join(f"  - {completion}" for completion in habit.completions)
        if habit.completions
        else "  No completions yet."
    )

    return "\n".join(
        [
            f"Name: {habit.name}",
            f"Description: {habit.description}",
            f"Periodicity: {habit.periodicity}",
            f"Created at: {habit.created_at}",
            "Completions:",
            completion_times,
        ]
    )


def group_habits_based_on_periodicity(habit_list: list[Habit]) -> str:
    periodicities = ("daily", "weekly")

    return "\n\n".join(
        (
            f"{periodicity.capitalize()} habits:\n"
            + "\n".join(
                f"{index}. {habit.name}"
                for index, habit in enumerate(
                    (habit for habit in habit_list if habit.periodicity == periodicity),
                    start=1,
                )
            )
        )
        for periodicity in periodicities
    )


def get_longest_streak_for_habit(habit: Habit):
    periods = habit.get_periods_since_creation()

    completions_list = [
        int(
            any(
                (
                    habit.created_at
                    + timedelta(days=PERIODICITY_DAY_COUNT[habit.periodicity] * period)
                )
                <= completion
                < (
                    habit.created_at
                    + timedelta(
                        days=PERIODICITY_DAY_COUNT[habit.periodicity] * (period + 1)
                    )
                )
                for completion in habit.completions
            )
        )
        for period in range(periods)
    ]

    return max(
        (
            len(segment.replace("0", ""))
            for segment in "".join(map(str, completions_list)).split("0")
        ),
        default=0,
    )


def get_longest_streak_overall(habit_list: list[Habit]):
    return max(
        ((habit, get_longest_streak_for_habit(habit)) for habit in habit_list),
        key=lambda item: item[1],
        default=(None, 0),
    )
