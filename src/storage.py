import json
import os

#path to data file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, "data", "habits.json")

def load_data():
    """Reads JSON file and returns a python dictionary"""

    if not os.path.exists(DATA_FILE):
        #returns a default if datafile doesn't exist yet
        return {"habits": []}
    
    with open(DATA_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            #Handles empty or corrupted files
            return {"habits": []}
        
def save_data(data):
    """Writes a python dict to the JSON file"""
    
    #Ensure directory exists
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

    with open(DATA_FILE, "w") as file:
        # 'indent=4' makes JSON file human readable
        json.dump(data, file, indent=4)

