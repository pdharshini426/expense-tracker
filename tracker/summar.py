from datetime import datetime
from tracker.read import readjson

def summary(month):
    total = 0
    with open("tracker.json", "r") as file:
       track = readjson()
    
    if month is not None:
        flag = 0
        for track1 in track:
           date_string = track1["Date"]
           date_object = datetime.strptime(date_string, "%Y-%m-%d")
           month1 = date_object.month
           if month == month1:
            total += track1['Amount']
            flag = 1
        if flag == 0: 
           print(f"Entered month-{month} is not in the list ")
        else:
           print(f"Total expenses for {month1}: $",total)
    else:
        for track1 in track:
            total += track1['Amount']
        print("Total expenses: $",total)