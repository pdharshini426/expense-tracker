import json
from tracker.read import readjson

def delete(id):
   track = readjson()
   flag = 0
   if id is not None:
        for track1 in track:
         if track1["id"]==id:
             flag = 1 
             track.remove(track1)
             with open("tracker.json", "w") as file:
                     json.dump(track,file)
                     print(f"Expense {id} deleted successfully")
        if flag == 0:
         print(f"Expense {id} not in the list")
   else:
       print("--id cant be empty")
      
      