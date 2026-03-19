# Habit Tracker

## Description
A simple CLI habit tracking tool.

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

## Planned Updates

### Data Management & Recovery

[X] Archive View: Add a --show-deleted flag to the list command to view soft-deleted habits.  
[X] Restore Function: Implement a restore id command to flip the active status back to True.  
[ ] Data Export: Add a command to export habit history to a CSV format for external analysis.  

### Customization & UI

[X] Custom Indicators: Allow users to define their own "Success" and "Failure" icons (e.g., habit set-icon check "✅" or habit set-icon x "❌").  
[X] Colorized Output: Integrate terminal color codes (ANSI) to highlight streaks or urgent tasks.  
[ ] Progress Bars: Implement a stats view with visual bars representing weekly completion percentages.  

### Logic Enhancements

[ ] Habit Categories: Group habits by tags (e.g., #Language, #Fitness, #Coding).  
[ ] Reminder System: Simple CLI notification check if habits aren't completed by a certain hour.  
[ ] Time-Travel Debugging: An internal developer command to manually adjust dates for testing streak logic.  

## TUI Upgrade Plan

### Interface & Layout
[ ] The "Split-Pane" Dashboard:

- Left Sidebar: Live-filtering list of habits.

- Main Stage: Dynamic area for Stats, Heatmaps, and Input forms.

- Status Bar: Bottom-row progress tracker (e.g., Progress: [###-------] 30%).

[ ] Live Search: Top-bar input that filters the sidebar in real-time as you type.

[ ] Viewport Clipping: Support for scrolling long lists of habits within the terminal height.

### Navigation (The "Arrow Key Household" Standard)
[ ] Selection Logic: Use Up/Down Arrows to highlight habits in the sidebar.

[ ] Quick-Action: Hit Enter to toggle the completion status (✅/❌) of the highlighted habit.

[ ] Detail Toggle: Hit Tab to swap the Main Stage between "Global Stats" and "Habit Detail View."

[ ] The "Quick-Add" Flow: Hit Space or Ctrl+A to instantly clear the Dashboard for a new habit entry.

[ ] Safe Archive: Hit Delete to trigger a confirmation prompt before soft-deleting a habit.

### Data & Deep Insights
[ ] GitHub-style Heatmap: A visual grid showing completion history over the last 90 days.

[ ] The show id View: Detailed breakdown including:

- Creation Date

- Lifetime Total Completions

- Personal Best (Longest Streak)

[ ] Advanced Sorting: Toggle between Newest, Alphabetical, or "Highest Streak" order.

[ ] Archive Vault: Use a --show-deleted flag (or a TUI toggle) to view and Restore inactive habits.

### Universal & Pro Features
[ ] The config.json System: Allow users to define custom icons, themes, and keybindings (for those weirdos who want Vim keys).

[ ] Standalone Distribution: Prepare the project for PyInstaller (.exe) and an AUR PKGBUILD (.pkg.tar.zst).

[ ] GitHub Data Sync: Option to automatically push/pull the habits.json to a dedicated private repository.
