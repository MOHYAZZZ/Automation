import sys
import clipboard
import json

STORED_DATA = "clipboard.json"


def save_values(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)


def load_values(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data

    except:
        return {}


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_values(STORED_DATA)

    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_values(STORED_DATA, data)
        print("Data has been saved.")

    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data has been copied to clipboard.")

        else:
            print("Key does not exist!")

    elif command == "list":
        print(data)
    else:
        print("Unknown command!")
else:
    print("Please enter exactly one command.")
