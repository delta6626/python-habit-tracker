from Habit import Habit
    
def view_all_habits(habits: list[Habit]) -> str:
    return "\n".join(
        map(
            lambda item: f"{item[0]}. {item[1].name}",
            enumerate(habits, start=1)
        )
    )