# Habit Tracker

## Description
A simple CLI habit tracking tool.

## Planned Updates

### Data Management & Recovery

[ ] Archive View: Add a --show-deleted flag to the list command to view soft-deleted habits.  
[ ] Restore Function: Implement a restore id command to flip the active status back to True.  
[ ] Data Export: Add a command to export habit history to a CSV format for external analysis.  

### Customization & UI

[ ] Custom Indicators: Allow users to define their own "Success" and "Failure" icons (e.g., habit set-icon check "✅" or habit set-icon x "❌").  
[ ] Colorized Output: Integrate terminal color codes (ANSI) to highlight streaks or urgent tasks.  
[ ] Progress Bars: Implement a stats view with visual bars representing weekly completion percentages.  

### Logic Enhancements

[ ] Habit Categories: Group habits by tags (e.g., #Language, #Fitness, #Coding).  
[ ] Reminder System: Simple CLI notification check if habits aren't completed by a certain hour.  
[ ] Time-Travel Debugging: An internal developer command to manually adjust dates for testing streak logic.  

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