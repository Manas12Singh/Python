import json

with open("students.json") as file:
    data = {"Manas Singh": json.load(file)['Manas Singh']}

data["Manas Singh"]["Name"] = "Manas"

