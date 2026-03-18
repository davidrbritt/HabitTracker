from storage import load_data, save_data
from datetime import date
def add_habit(name):
    data = load_data()

    #ID generation
    new_id = len(data["habits"]) + 1

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

