from storage import load_data, save_data
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
    #Filter: Show everything if show_all is True, otherwise only active habits
    habits_to_show = data["habits"] if show_all else [h for h in data["habits"] if h.get("active", True)]
    if not habits_to_show:
        print("No habits found. Use 'add' to create one! (Try --show-deleted if you have archived ones!)")
        return
    
    print("\n--- Your Active Habits ---")
    print(f"{'ID':<4} | {'Habit Name':<30} | {'Streak':<7}")
    print("-" * 45)

    for habit in habits_to_show:
        #Add a checkmark if done today
        check_mark = "✅"
        x_mark = "❌"
        today = str(date.today())
        status = check_mark if today in habit["completed_dates"] else x_mark
        
        # Add a visual indicator for archived habits
        is_active = habit.get("active", True)
        display_name = habit['task']
        if not is_active:
            display_name += " [ARCHIVED]"
        
        print(f"{status} {habit['id']:<4} | {display_name:<30} | {habit['streak']:<7}")
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