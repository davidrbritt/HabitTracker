# Habit Tracker

### File Structure

---

habit-tracker/  
├── data/                   # Directory for persistent storage  
│   └── habits.json         # Where habits and logs live  
├── src/                    # All source code  
│   ├── __init__.py         # Makes 'src' a package  
│   ├── main.py             # Entry point (handles CLI arguments)  
│   ├── manager.py          # Logic for adding/completing habits  
│   └── storage.py          # Logic for reading/writing to JSON  
├── tests/                  # Unit tests for logic  
│   └── test_manager.py  
├── .gitignore              
├── README.md               # Documentation on how to use the CLI  
└── requirements.txt        # List of any external libraries used  

---