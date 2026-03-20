from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, ListItem, ListView, Label
from storage import load_data # Assuming your CLI file is storage.py

class HabitApp(App):
    BINDINGS = [("q", "quit", "Quit")]

    def compose(self) -> ComposeResult:
        yield Header()
        
        # Load your actual data
        habits = load_data()
        
        # We wrap the habits in a ListView (a scrollable list)
        with ListView():
            for h in habits.get('habits', []):
                if h.get("active", True):
                    yield ListItem(Label(f"ID: {h['id']} | {h['task']} | Streak: {h['streak']}"))
        
        yield Footer()

if __name__ == "__main__":
    app = HabitApp()
    app.run()