from HabitServiceProvider import HabitServiceProvider
from utilities import get_input_within_range
import constants

habit_service_provider = HabitServiceProvider()


def main():
    """
    The main function serves as the entrypoint to the application.
    """

    print("Welcome to the habit tracker application")
    print(constants.MENU_OPTIONS_TEXT)

    while True:

        chosen_option = get_input_within_range(
            "[MAIN MENU] - What action would you like to perform?: ",
            1,
            len(constants.MENU_OPTIONS),
            constants.INVALID_INPUT_TEXT,
            constants.VALUE_ERROR_MESSAGE,
        )

        if chosen_option == constants.MENU_OPTIONS["add_habit"]:
            habit_service_provider.initiate_add_new_habit()
        elif chosen_option == constants.MENU_OPTIONS["complete_habit"]:
            habit_service_provider.initiate_check_off_habit()
        elif chosen_option == constants.MENU_OPTIONS["delete_habit"]:
            habit_service_provider.initiate_delete_habit()
        elif chosen_option == constants.MENU_OPTIONS["view_analytics"]:
            habit_service_provider.initiate_view_analytics()
        elif chosen_option == constants.MENU_OPTIONS["repeat_menu"]:
            print(constants.MENU_OPTIONS_TEXT)
        elif chosen_option == constants.MENU_OPTIONS["exit"]:
            print("Goodbye.")
            break
        else:
            print(constants.INVALID_INPUT_TEXT)


if __name__ == "__main__":
    main()
