import sys
import pyperclip
import json

SAVE_DATA = "clipboard.json"

def save_stuff(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)


def  load_json(filepath):
    try:
        with  open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}



if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_json(SAVE_DATA)

    if command == "save":
        key = input("Enter a key: ")
        data[key] = pyperclip.paste()
        save_stuff(SAVE_DATA, data)
        print("Data is saved!")

    elif command == "load":
        key  = input("Enter a Key: ")
        if key in data:
            pyperclip.copy(data[key])
            print('Data copy to the clipboard')
        else:
            print('Key does not exist!')

    elif  command == "list":
        print(data)
    else:
        print("Unknown command")
else:
    print("Please provide only one command!")


