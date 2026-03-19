from storage import load_data, save_data, load_config, save_config
from datetime import date, timedelta
def add_habit(name):
    data = load_data()

    #ID generation
    # Get all existing IDs. If the list is empty, start at 0.
    existing_ids = [h["id"] for h in data["habits"]]
    new_id = max(existing_ids, default=0) + 1

    new_habit = {
        "id": new_id,
        "task": name,
        "created_at": str(date.today()),
        "completed_dates": [],
        "streak": 0,
        "active": True    
    }
    data["habits"].append(new_habit)
    save_data(data)
    print(f"SUCCESS - Added habit: {name} (ID: {new_id})")

def complete_habit(habit_id):
    """Marks a habit as complete for the day. Handles logic for streaks too."""
    data = load_data()
    today = str(date.today())
    yesterday = str(date.today() - timedelta(days=1))

    for habit in data["habits"]:
        if habit["id"] == habit_id:
            #Handle habits that are already done for the day
            if today in habit["completed_dates"]:
                print(f"! Habit '{habit['task']}' already completed today.")
                return
            
            #Update habit streak logic
            if habit["completed_dates"] and habit["completed_dates"][-1] == yesterday:
                habit["streak"] += 1
            else:
                habit["streak"] = 1

            habit["completed_dates"].append(today)
            save_data(data)
            print(f"SUCCESS! {habit['task']} streak is now {habit['streak']}!")
            return
    print(f"ERROR: No habit found with ID {habit_id}!")

def list_habits(show_all=False):
    data = load_data()
    config = load_config()
    #Set icons to the user selected options in their config.json
    check_mark = config["icons"].get("success", "✅")
    x_mark = config["icons"].get("failure", "❌")
    #Filter: Show everything if show_all is True, otherwise only active habits
    habits_to_show = data["habits"] if show_all else [h for h in data["habits"] if h.get("active", True)]
    if not habits_to_show:
        print("No habits found. Use 'add' to create one! (Try --show-deleted if you have archived ones!)")
        return
    
    print("\n--- Your Active Habits ---")
    print(f"{'ID':<4} | {'Habit Name':<30} | {'Streak':<7}")
    print("-" * 45)

    # ANSI Color Codes
    GREEN = "\033[92m"
    RED = "\033[91m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    for habit in habits_to_show:

        #Add a checkmark if done today
        # Status icon color (Success = Green, Failure = Red)
        today = str(date.today())
        is_done = today in habit["completed_dates"]
        icon_color = GREEN if is_done else RED
        status = f"{icon_color}{check_mark if is_done else x_mark}{RESET}"

        #Streak Color (High Bold Green, no streak red)
        streak = habit['streak']
        if streak >= 3:
            streak_str = f"{GREEN}{BOLD}{streak}{RESET}"
        elif streak > 0:
            streak_str = f"{GREEN}{streak}{RESET}"
        else:
            streak_str = f"{RED}{streak}{RESET}"


        # Add a visual indicator for archived habits
        is_active = habit.get("active", True)
        #display_name = habit['task']
        #if not is_active:
        #    display_name += f"  {CYAN}[ARCHIVED]{RESET}"

        #Start with task name
        task_name = habit['task']

        #Add [ARCHIVED] tag without color to fix padding issue
        if not is_active:
            full_display = f"{task_name} [ARCHIVED]"
        else:
            full_display = task_name
        
        #Apply padding  to plain text (30 characters)
        padded_display = f"{full_display:<30}"

        #Inject the color into the padded text for the tag only
        if not is_active:
            #Replace plain tag with color one
            final_display = padded_display.replace("[ARCHIVED]", f"{CYAN}[ARCHIVED]{RESET}")
        else:
            final_display = padded_display

        print(f"{status} {habit['id']:<4} | {final_display} | {streak_str}")
    print("\n")

def delete_habit(habit_id):
    data = load_data()
    found = False
    
    for habit in data["habits"]:
        if habit["id"] == habit_id:
            habit["active"] = False
            found = True
            break
            
    if found:
        save_data(data)
        print(f"SUCCESS: Habit {habit_id} has been archived.")
    else:
        print(f"ERROR: Habit {habit_id} not found.")

def restore_habit(habit_id):
    data = load_data()
    found = False

    for habit in data["habits"]:
        if habit["id"] == habit_id:
            if habit.get("active", True) == True:
                print(f"ERROR: Habit id {habit_id} is already active. . .")
                found = True
                return
            
            habit["active"] = True
            found = True
            save_data(data)
            print(f"SUCCESS: Habit {habit_id} ('{habit['task']}') has been restored.")
            break
    
    if not found:
        print(f"ERROR: Habit {habit_id} not found.")

def update_icon(icon_type = None, new_icon = None, use_default = False):
    config = load_config()

    if use_default:
        #Reset to def keys in config.json
        config["icons"]["success"] = config["icons"].get("defsuccess", "✅")
        config["icons"]["failure"] = config["icons"].get("deffailure", "❌")
        save_config(config)
        print("SUCCESS: Icons have been reset to default settings.")
        return
    
    if not icon_type or not new_icon:
        print("ERROR: Please specify a which icon to replace (success/failure) and an icon or use --default.")

    if icon_type in ["success", "failure"]:
        config["icons"][icon_type] = new_icon
        save_config(config)
        print(f"SUCCESS: {icon_type.capitalize()} icon updated to : {new_icon}")
    else:
        print("ERROR: Icon type must be either 'success' or 'failure'.")