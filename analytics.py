from Habit import Habit
from datetime import datetime, timedelta
from constants import PERIODICITY_DAY_COUNT


def get_all_habits(habits: list[Habit]) -> str:
    """
    Return a numbered list containing the names of all habits.

    Args:
        habits: The list of habits to display.

    Returns:
        A numbered list containing the names of all habits.
    """

    return "\n".join(
        map(lambda item: f"{item[0]}. {item[1].name}", enumerate(habits, start=1))
    )


def get_habit_details(habit: Habit) -> str:
    """
    Return the details of a habit, including all of its completion
    records, in a readable format.

    Args:
        habit: The habit whose details should be displayed.

    Returns:
        A formatted string containing the habit's details.
    """

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
    """
    Return all habits grouped based on their periodicity.

    Args:
        habit_list: The list of habits to group.

    Returns:
        A formatted string containing the habits grouped by periodicity.
    """

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


def get_longest_streak_for_habit(
    habit: Habit, datetime_of_check: datetime | None = None
) -> int:
    """
    Calculate and return the longest consecutive completion streak for the specified habit.

    The habit's periodicity determines the period length. Each period is
    marked as completed if there is at least one completion record that
    occurred during that period. A missed period (period with no completions)
    breaks the streak, and the longest consecutive sequence of completed
    periods is returned.

    Args:
        habit: The habit for which the longest streak should be calculated.
        datetime_of_check: The date and time used as the reference point.

    Returns:
        The length of the longest consecutive completion streak.
    """

    now = datetime_of_check or datetime.now()
    periods = habit.get_current_period_number(now)

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


def get_longest_streak_overall(habit_list: list[Habit]) -> tuple[Habit | None, int]:
    """
    Find and return the habit with the longest streak overall.

    Uses the get_longest_streak_for_habit function to find the longest
    streak for each habit. The habit with the longest streak overall
    is then identified and returned together with its streak length.

    Args:
        habit_list: The list of habits to evaluate.

    Returns:
        A tuple containing the habit with the longest streak and its streak length.
    """

    return max(
        ((habit, get_longest_streak_for_habit(habit)) for habit in habit_list),
        key=lambda item: item[1],
        default=(None, 0),
    )
