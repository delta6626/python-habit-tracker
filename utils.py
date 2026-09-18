import json

file_name = "config.json"


def is_test_data_loaded() -> bool:
    try:
        with open(file_name, "r") as file:
            config_data = json.load(file)
            return config_data["test_data_loaded"]

    except (FileNotFoundError, KeyError):
        config_data = {"test_data_loaded": False}

        with open(file_name, "w") as file:
            json.dump(config_data, file)

        return False


def update_test_data_status(status: bool) -> None:
    try:
        with open(file_name, "r") as file:
            config_data = json.load(file)

        config_data["test_data_loaded"] = status

        with open(file_name, "w") as file:
            json.dump(config_data, file)

    except (FileNotFoundError, KeyError):
        config_data = {"test_data_loaded": status}

        with open(file_name, "w") as file:
            json.dump(config_data, file)
