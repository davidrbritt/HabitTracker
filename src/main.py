import argparse
from manager import add_habit, complete_habit, list_habits, delete_habit, restore_habit, update_icon

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

    #Setup the 'delete' command
    delete_parser = subparsers.add_parser("delete", help="Archive a habit")
    delete_parser.add_argument("id", type=int, help="The ID of the habit to archive")

    # Setup the 'set-icon' command
    icon_parser = subparsers.add_parser("set-icon", help="Change completion icons")
    # nargs="?" makes these optional so --default works by itself
    icon_parser.add_argument("type", choices=["success", "failure"], nargs="?", help="Icon type")
    icon_parser.add_argument("icon", nargs="?", help="The emoji/symbol to use")
    icon_parser.add_argument("--default", action="store_true", help="Reset to defaults")

    # Setup the 'restore' command
    restore_parser = subparsers.add_parser("restore", help="Restore an archived habit")
    restore_parser.add_argument("id", type=int, help="The ID of the habit to restore")

    #Setup the 'list' command
    list_parser = subparsers.add_parser("list", help="Show all active habits and streaks")
    list_parser.add_argument('--show-deleted', action='store_true')
    #Parse the arguments
    args = parser.parse_args()

    #Route the command to the right Manager function
    if args.command == "add":
        add_habit(args.name)
    elif args.command == "done":
        complete_habit(args.id)
    elif args.command == "restore":
        restore_habit(args.id)
    elif args.command == "list":
        list_habits(show_all=args.show_deleted)
    elif args.command == "set-icon":
        update_icon(args.type, args.icon, args.default)
    elif args.command == "delete":
        delete_habit(args.id)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()