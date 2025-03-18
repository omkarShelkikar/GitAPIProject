import json
import os

file_path = os.path.join(os.path.dirname(__file__), "../config/env.json")


def load_config():
    try:
        with open(file_path, 'r') as file:
           data = json.load(file)
           return data
    except (FileNotFoundError) as e:
        print(f"Error reading config file: {e}")
        raise

config_data = load_config()
def getAPIkey():
    return config_data.get("api_key",None)


def getBaseUrl():
    return config_data.get("base_url",None)

