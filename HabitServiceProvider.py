from HabitDatabase import HabitDatabase
from datetime import datetime
from Habit import Habit
from input_utilities import (
    get_non_empty_input,
    get_periodicity_input,
    get_input_within_range,
)
import analytics
import constants


class HabitServiceProvider:
    """
    Coordinates habit-related operations between the user interface,
    habit data, database, and analytics modules.
    """

    def __init__(self):
        """
        Initialize the database connection and load all stored habits.
        """

        self.database = HabitDatabase()
        self.habit_list = self.database.get_all_habits()

    def sort_habits_latest_first(self) -> list[Habit]:
        """
        Return the habits sorted by creation date, with the newest one appearing first (reverse chronological order).
        """

        sorted_habits = sorted(
            self.habit_list, key=lambda habit: habit.created_at, reverse=True
        )
        return sorted_habits

    def initiate_view_all_habits(self) -> None:
        """
        Display all habits in reverse chronological order.
        """

        if not self.habit_list:
            print("\nYou have no habits yet. Add one first.\n")
            return

        sorted_habits = self.sort_habits_latest_first()
        print("\nHere is a list of all your habits (latest first): ")
        print(f"{analytics.get_all_habits(sorted_habits)}\n")

    def initiate_view_habit_details(self) -> None:
        """
        Prompt the user to select a habit and display its details.
        """

        if not self.habit_list:
            print("\nYou have no habits yet. Add one first.\n")
            return

        self.initiate_view_all_habits()
        sorted_habits = self.sort_habits_latest_first()
        habit_identifier = get_input_within_range(
            "[HABIT SELECTION] - Which habit would you like to learn more about?: ",
            1,
            len(sorted_habits),
            constants.INVALID_HABIT_IDENTIFIER,
            constants.VALUE_ERROR_MESSAGE,
        )

        chosen_habit = sorted_habits[habit_identifier - 1]
        print("\nHere are the details for your selected habit:\n")
        print(f"{analytics.get_habit_details(chosen_habit)}\n")

    def initiate_view_habits_with_same_periodicity(self):
        """
        Group habits based on their periodicity and display them.
        """

        if not self.habit_list:
            print("\nYou have no habits yet. Add one first.\n")
            return

        print("\nHere are your habits grouped by periodicity:\n")
        print(f"{analytics.group_habits_based_on_periodicity(self.habit_list)}\n")

    def initiate_view_longest_streak_for_habit(self) -> None:
        """
        Prompt the user to select a habit and display its longest streak.
        """

        if not self.habit_list:
            print("\nYou have no habits yet. Add one first.\n")
            return

        self.initiate_view_all_habits()
        sorted_habits = self.sort_habits_latest_first()
        habit_identifier = get_input_within_range(
            "[HABIT SELECTION] - Select a habit to check its longest streak: ",
            1,
            len(sorted_habits),
            constants.INVALID_HABIT_IDENTIFIER,
            constants.VALUE_ERROR_MESSAGE,
        )

        chosen_habit = sorted_habits[habit_identifier - 1]
        print(
            f"\nThe longest streak for '{chosen_habit.name}' is {analytics.get_longest_streak_for_habit(chosen_habit)}.\n"
        )

    def initiate_view_longest_streak_overall(self) -> None:
        """
        Display the habit with the longest streak overall.
        """

        if not self.habit_list:
            print("\nYou have no habits yet. Add one first.\n")
            return

        habit, streak = analytics.get_longest_streak_overall(self.habit_list)
        print(f"\nThe habit '{habit.name}' has the longest streak.")
        print(f"It has lasted for {streak} periods.\n")

    def initiate_add_new_habit(self) -> None:
        """
        Prompt the user for the required habit information and add the new habit
        to the database and in-memory habit list.
        """

        habit_name = get_non_empty_input(
            "Habit name", "\nEnter a name for your new habit: "
        )
        habit_description = input(
            "Enter a description for your new habit (optional): "
        ).strip()
        habit_periodicity = get_periodicity_input(
            "Enter the desired periodicity for your habit (daily/weekly): "
        )

        new_habit = Habit(
            None, habit_name, habit_description, habit_periodicity, datetime.now(), []
        )
        self.database.add_habit(new_habit)
        self.habit_list.append(new_habit)
        print("New habit added successfully.\n")

    def initiate_check_off_habit(self) -> None:
        if not self.habit_list:
            print("\nYou have no habits yet. Add one first.\n")
            return

        self.initiate_view_all_habits()

        sorted_habits = self.sort_habits_latest_first()
        habit_identifier = get_input_within_range(
            "[HABIT SELECTION] - Enter the identifier of the habit you would like to check off: ",
            1,
            len(sorted_habits),
            constants.INVALID_HABIT_IDENTIFIER,
            constants.VALUE_ERROR_MESSAGE,
        )

        chosen_habit = sorted_habits[habit_identifier - 1]
        current_time = datetime.now()
        self.database.check_off_habit(chosen_habit.id, current_time)
        chosen_habit.check_off_habit(current_time)

        print(
            f"Habit #{habit_identifier} - '{chosen_habit.name}' was checked off at {current_time.isoformat()}.\n"
        )

    def initiate_delete_habit(self) -> None:
        if not self.habit_list:
            print("\nYou have no habits yet. Add one first.\n")
            return

        self.initiate_view_all_habits()

        sorted_habits = self.sort_habits_latest_first()
        habit_identifier = get_input_within_range(
            "[HABIT SELECTION] - Enter the identifier of the habit you would like to delete: ",
            1,
            len(sorted_habits),
            constants.INVALID_HABIT_IDENTIFIER,
            constants.VALUE_ERROR_MESSAGE,
        )

        chosen_habit = sorted_habits[habit_identifier - 1]
        self.database.delete_habit(chosen_habit.id)
        self.habit_list.remove(chosen_habit)

        print(
            f"Habit #{habit_identifier} - '{chosen_habit.name}' was deleted successfully.\n"
        )

    def initiate_view_analytics(self) -> None:
        print("\nAvailable analytics: ")
        print(constants.ANALYTICS_OPTIONS_TEXT)

        chosen_option = get_input_within_range(
            "[ANALYTICS MENU] - Which one would you like to see?: ",
            1,
            len(constants.ANALYTICS_OPTIONS),
            constants.INVALID_ANALYTICS_OPTION,
            constants.VALUE_ERROR_MESSAGE,
        )

        if chosen_option == constants.ANALYTICS_OPTIONS["get_all_habits"]:
            self.initiate_view_all_habits()
        elif chosen_option == constants.ANALYTICS_OPTIONS["get_habit_details"]:
            self.initiate_view_habit_details()
        elif (
            chosen_option
            == constants.ANALYTICS_OPTIONS["get_all_habits_with_same_periodicity"]
        ):
            self.initiate_view_habits_with_same_periodicity()
        elif (
            chosen_option == constants.ANALYTICS_OPTIONS["get_longest_streak_for_habit"]
        ):
            self.initiate_view_longest_streak_for_habit()
        elif chosen_option == constants.ANALYTICS_OPTIONS["get_longest_streak_overall"]:
            self.initiate_view_longest_streak_overall()
