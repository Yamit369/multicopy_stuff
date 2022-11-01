import sys
import pyperclip
import json

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

