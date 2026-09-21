from Habit import Periodicity


def get_non_empty_input(value_name: str, prompt: str) -> str:
    """
    Prompt the user for a non-empty text value.

    Repeats the prompt until the user provides a value containing
    at least one non-whitespace character.
    """

    while True:
        input_value = input(prompt).strip()

        if input_value:
            return input_value

        print(f"Invalid input. {value_name} cannot be empty.")


def get_periodicity_input(prompt: str) -> Periodicity:
    """
    Prompt the user for a valid habit periodicity.

    Repeats the prompt until the user enters a valid periodicity.
    The input is converted to lowercase before validation.
    """

    while True:
        input_value = input(prompt).strip().lower()

        if input_value in ("daily", "weekly"):
            return input_value

        print("Invalid periodicity. Please enter daily or weekly.")


def get_input_within_range(
    prompt: str,
    min_allowed: int,
    max_allowed: int,
    on_invalid_range: str,
    on_value_error: str,
) -> int:
    """
    Prompt the user for an integer within a specified range.

    Repeats the prompt when the input is not an integer or falls
    outside the specified range.
    """

    while True:
        try:
            input_value = int(input(prompt))

            if min_allowed <= input_value <= max_allowed:
                return input_value

            print(on_invalid_range)
        except ValueError:
            print(on_value_error)
