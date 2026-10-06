import json
from datetime import date


def add(description,amount):
    track = []
    with open("tracker.json", "r") as file:
      track = json.load(file)
      if len(track)==0:
        new_id = 1
      else:
        new_id = track[-1]["id"] + 1


    if amount and description is not None:
       dict_ = {
       "id": new_id,
       "Date": str(date.today()),
       "Description": description,
       "Amount" : amount
      }
    else:
          print("Amount and description should not be empty")

    track.append(dict_)
    with open("tracker.json", "w") as file:
         json.dump(track,file)
         print(f"Expense added successfully (ID: {new_id})",)