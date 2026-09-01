from Habit import Habit


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


def get_longest_streak(habit_list: list[Habit]) -> str:
    pass
