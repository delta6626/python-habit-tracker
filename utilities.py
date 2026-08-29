from Habit import Periodicity

def get_non_empty_input(value_name: str, prompt: str) -> str:
    while True:
        input_value = input(prompt).strip()

        if input_value:
            return input_value

        print(f"Invalid input. {value_name} cannot be empty.")

def get_periodicity_input(prompt: str) -> Periodicity:
    while True:
        input_value = input(prompt).strip().lower()

        if input_value in ("daily", "weekly"):
            return input_value

        print("Invalid periodicity. Please enter daily or weekly.")

def get_habit_number_input(prompt:str, min_allowed: int, max_allowed:int) -> int:
    while True:
        try:
            input_value = int(input(prompt))

            if min_allowed <= input_value <= max_allowed:
                return input_value
            
            print("Invalid identifier. Please enter a valid identifier.")
        except ValueError:
            print("Habit identifier should be a number.")