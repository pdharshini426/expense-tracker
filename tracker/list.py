import json

def list():
    with open("tracker.json", "r") as file:
          track = json.load(file)


    print(f"{'ID':<5} {'Date':<10} {'Description':<15} {'Amount':<10}")
    print("-" * 50)

    for expense in track:
      print(
        f"{expense['id']:<5} "
        f"{expense['Date']:<10} "
        f"{expense['Description']:<15} "
        f"{expense['Amount']:<10}"
      )