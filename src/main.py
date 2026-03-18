import argparse
from manager import add_habit, complete_habit, list_habits

def main():
    # 1. Create the main parser
    parser = argparse.ArgumentParser(description="Simple CLI Habit Tracker")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # 2. Setup the 'add' command
    add_parser = subparsers.add_parser("add", help="Add a new habit")
    add_parser.add_argument("name", type=str, help="The name of the habit (wrap in quotes if multiple words)")

    # 3. Setup the 'done' command
    done_parser = subparsers.add_parser("done", help="Mark a habit as completed")
    done_parser.add_argument("id", type=int, help="The ID number of the habit")

    # 4. Setup the 'list' command
    subparsers.add_parser("list", help="Show all active habits and streaks")

    # 5. Parse the arguments
    args = parser.parse_args()

    # 6. Route the command to the right Manager function
    if args.command == "add":
        add_habit(args.name)
    elif args.command == "done":
        complete_habit(args.id)
    elif args.command == "list":
        list_habits()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()