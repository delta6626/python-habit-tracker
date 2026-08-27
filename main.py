menu_options = {
    "view_habits": 1,
    "complete_habit": 2,
    "add_habit":3,
    "delete_habit": 4,
    "view_analytics": 5,
    "repeat_menu": 6,
    "exit": 7

}

menu_options_text = f"""
Press {menu_options['view_habits']} to view all created habits
Press {menu_options['complete_habit']} to complete/check-off a habit
Press {menu_options['add_habit']} to add a new habit
Press {menu_options['delete_habit']} to delete a habit
Press {menu_options['view_analytics']} to view analytics
Press {menu_options['repeat_menu']} to see the menu again
Press {menu_options['exit']} to exit
"""

invalid_input_text = f"Invalid option. Enter a valid one or press {menu_options['repeat_menu']} to view all valid options."

def main():
    """
    The main function serves as the entrypoint to the application.
    """

    print("Welcome to the habit tracker application")
    print(menu_options_text)

    while(True):
        try:
            chosen_option = int(input("Please enter your preferred option: "))
            if chosen_option == menu_options["view_habits"]:
                pass
            elif chosen_option == menu_options["complete_habit"]:
                pass
            elif chosen_option == menu_options["add_habit"]:
                pass
            elif chosen_option == menu_options["delete_habit"]:
                pass
            elif chosen_option == menu_options["view_analytics"]:
                pass
            elif chosen_option == menu_options["repeat_menu"]:
                print(menu_options_text)
            elif chosen_option == menu_options["exit"]:
                print("Goodbye.")
                break
            else:
                print(invalid_input_text)
        except ValueError:
            print(invalid_input_text);


if __name__ == "__main__":
    main()