import argparse
from manager import add_habit, complete_habit, list_habits, delete_habit

def main():
    #Create the main parser
    parser = argparse.ArgumentParser(description="Simple CLI Habit Tracker")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    #Setup the 'add' command
    add_parser = subparsers.add_parser("add", help="Add a new habit")
    add_parser.add_argument("name", type=str, help="The name of the habit (wrap in quotes if multiple words)")

    #Setup the 'done' command
    done_parser = subparsers.add_parser("done", help="Mark a habit as completed")
    done_parser.add_argument("id", type=int, help="The ID number of the habit")

    delete_parser = subparsers.add_parser("delete", help="Archive a habit")
    delete_parser.add_argument("id", type=int, help="The ID of the habit to archive")

    #Setup the 'list' command
    subparsers.add_parser("list", help="Show all active habits and streaks")
    
    #Parse the arguments
    args = parser.parse_args()

    #Route the command to the right Manager function
    if args.command == "add":
        add_habit(args.name)
    elif args.command == "done":
        complete_habit(args.id)
    elif args.command == "list":
        list_habits()
    elif args.command == "delete":
        delete_habit(args.id)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()