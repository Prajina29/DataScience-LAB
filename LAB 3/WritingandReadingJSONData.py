# 4. Writing and Reading JSON Data
# ● Stores student details (ID, name, and marks) in a JSON file
# ● Reads the JSON file and displays the student information
# ● Handles exceptions related to file access and JSON decoding

import json

students = {
    "1": {"name": "Dipti", "marks": 85},
    "2": {"name": "Ram", "marks": 90},
    "3": {"name": "Sita", "marks": 78}
}

try:
    with open("students.json", "w") as f:
        json.dump(students, f) # dump ley lekhcha 
except IOError:
    print("Error writing file")

try:
    with open("students.json", "r") as f:
        data = json.load(f) # load ley return garcha 
        print(data)

    for id, info in data.items():
        print("ID:", id)
        print("Name:", info["name"])
        print("Marks:", info["marks"])
        print()

except FileNotFoundError:
    print("File not found")
except json.JSONDecodeError:
    print("Invalid JSON data")
