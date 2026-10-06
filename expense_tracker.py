import argparse
import json
import os
from tracker.add import add
from tracker.list import list
from tracker.delete import delete
from tracker.summar import summary

if not os.path.exists("tracker.json"):
    with open("tracker.json", "w") as file:
        json.dump([], file)

#created parser object that will handle Command line
parser = argparse.ArgumentParser()

# expects argument
parser.add_argument("tracker", choices=["add","list","delete","summary"])

#--decription means optional argument must be mentioned in the command "--description"
parser.add_argument("--description", type=str)
parser.add_argument("--amount", type=float)
parser.add_argument("--id", type=int)
parser.add_argument("--month", type=int)

# reads the command
args = parser.parse_args()


match args.tracker:
    case "add":
     add(args.description,args.amount)

    case "list":
      list()

    case "delete":
      delete(args.id)

    case "summary":
      summary(args.month)






