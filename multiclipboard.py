import sys
import pyperclip
import json

def save_stuff(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)


def  load_json(filepath):
    with  open(filepath, "r") as f:
        data = json.load(f)
        return data


if len(sys.argv) == 2:
    command = sys.argv[1]
    print(command)

    if command == "save":
        print("save")
    elif command == "load":
        print("load")
    elif  command == "list":
        print("list")
    else:
        print("Unknown command")
else:
    print("Please provide only one command!")


