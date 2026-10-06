import json


def delete(id):
     with open("tracker.json", "r") as file:
        track = json.load(file)
     flag = 0
     for track1 in track:
         
         if track1["id"]==id:
             flag = 1
             track.remove(track1)
             with open("tracker.json", "w") as file:
                     json.dump(track,file)
                     print(f"Expense {id} deleted successfully")
     if flag == 0:
        print(f"Expense {id} not in the list")