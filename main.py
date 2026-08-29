from HabitManager import HabitManager
import constants

habit_manager = HabitManager()

def main():
    """
    The main function serves as the entrypoint to the application.
    """

    print("Welcome to the habit tracker application")
    print(constants.MENU_OPTIONS_TEXT)

    while(True):
        try:
            chosen_option = int(input("What action would you like to perform?: "))

            if chosen_option == constants.MENU_OPTIONS["add_habit"]:
                habit_manager.add_new_habit()
            elif chosen_option == constants.MENU_OPTIONS["complete_habit"]:
                pass
            elif chosen_option == constants.MENU_OPTIONS["delete_habit"]:
                pass
            elif chosen_option == constants.MENU_OPTIONS["view_analytics"]:
                pass
            elif chosen_option == constants.MENU_OPTIONS["repeat_menu"]:
                print(constants.MENU_OPTIONS_TEXT)
            elif chosen_option == constants.MENU_OPTIONS["exit"]:
                print("Goodbye.")
                break
            else:
                print(constants.INVALID_INPUT_TEXT)
        except ValueError:
            print(constants.INVALID_INPUT_TEXT)


if __name__ == "__main__":
    main()