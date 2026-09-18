import json

config_file_name = "config.json"


def is_demo_data_loaded() -> bool:
    try:
        with open(config_file_name, "r") as file:
            config_data = json.load(file)
            return config_data["demo_data_loaded"]

    except (FileNotFoundError, KeyError):
        config_data = {"demo_data_loaded": False}

        with open(config_file_name, "w") as file:
            json.dump(config_data, file)

        return False


def update_demo_data_status(status: bool) -> None:
    try:
        with open(config_file_name, "r") as file:
            config_data = json.load(file)

        config_data["demo_data_loaded"] = status

        with open(config_file_name, "w") as file:
            json.dump(config_data, file)

    except (FileNotFoundError, KeyError):
        config_data = {"demo_data_loaded": status}

        with open(config_file_name, "w") as file:
            json.dump(config_data, file)
