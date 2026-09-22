from Habit import Periodicity


def get_non_empty_input(value_name: str, prompt: str) -> str:
    """
    Prompt the user for a non-empty text value. Repeat the prompt until the
    user provides a value containing at least one non-whitespace character.

    Args:
        value_name: The name of the value being requested.
        prompt: The prompt displayed to the user.

    Returns:
        The user's non-empty input.
    """

    while True:
        input_value = input(prompt).strip()

        if input_value:
            return input_value

        print(f"Invalid input. {value_name} cannot be empty.")


def get_periodicity_input(prompt: str) -> Periodicity:
    """
    Prompt the user for a valid habit periodicity. Repeat the prompt until the
    user enters a valid periodicity.

    Args:
        prompt: The prompt displayed to the user.

    Returns:
        The periodicity entered by the user.
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
    Prompt the user for an integer within a specified range. Repeat the prompt when
    the input is not an integer or falls outside the specified range.

    Args:
        prompt: The prompt displayed to the user.
        min_allowed: The minimum accepted value.
        max_allowed: The maximum accepted value.
        on_invalid_range: The message displayed when the input is outside
            the allowed range.
        on_value_error: The message displayed when the input is not an integer.

    Returns:
        The user's integer input if it falls within the specified range.
    """

    while True:
        try:
            input_value = int(input(prompt))

            if min_allowed <= input_value <= max_allowed:
                return input_value

            print(on_invalid_range)
        except ValueError:
            print(on_value_error)
