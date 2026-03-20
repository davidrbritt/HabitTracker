from datetime import date
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, ListItem, ListView, Label, Input, Static
from textual.containers import Horizontal, Vertical, Container
from storage import load_data, save_data 

class HabitApp(App):
    CSS = """
    #sidebar {
        width: 30%;
        border-right: solid $primary;
        padding: 1;
    }
    #sidebar Label {
        padding: 0 1;
        margin-bottom: 1;
        color: $secondary;
        text-style: underline;
    }
    #main-stage {
        width: 70%;
        padding: 1;
        align: center middle;
    }
    #status-bar {
        height: 2;
        background: $surface;
        color: $text;
        border-top: solid $primary;
        content-align: center middle;
    }
    #habit-list {
    background: $surface;
    height: auto;
    border: none;
    }

    /* This handles the keyboard cursor highlighting */
#habit-list:focus > ListItem.--highlight {
    background: $accent;
    color: $text;
    text-style: bold;
}

/* This keeps it highlighted even if you click away to the search bar */
#habit-list > ListItem.--highlight {
    background: $accent-darken-1;
}

/* Mouse hover still works as a separate visual cue */
ListItem:hover {
    background: $accent-lighten-2;
}
    """
    BINDINGS = [("ctrl+q", "quit", "Quit")]

    def on_input_changed(self, event: Input.Changed) -> None:
        # This triggers every time you type a letter
        if event.input.id == "search-input":
            self.refresh_list(event.value)

    def compose(self) -> ComposeResult:
        yield Header()
        # Top-bar Live Search
        yield Input(placeholder="Search habits...", id="search-input")
        
        with Horizontal():
            # Left Sidebar
            with Vertical(id="sidebar"):
                yield Label("Your Habits", variant="title")
                yield ListView(id="habit-list")
            
            # Main Stage
            with Container(id="main-stage"):
                yield Static("Select a habit to see stats", id="details-view")
        
        # Bottom Status Bar
        yield Static("Progress: [###-------] 30%", id="status-bar")
        yield Footer()

    def on_mount(self) -> None:
        self.refresh_list()

    def refresh_list(self, filter_text: str = "") -> None:
        data = load_data()
        habits = data.get('habits', [])
        today = date.today().isoformat()
    
        list_view = self.query_one("#habit-list", ListView)
        list_view.clear()

        for h in habits:
            # 1. Logic: Determine the prefix
            is_done = today in h.get('completed_dates', [])
            prefix = "✅ " if is_done else "❌ "
        
            # 2. Logic: Apply a 'dim' effect if it's done (purely via string tags)
            task_text = h['task']
            if is_done:
                task_text = f"[dim]{task_text}[/]"

            # 3. Filter and Append
            if filter_text.lower() in h['task'].lower():
                item = ListItem(Label(f"{prefix}{task_text}"))
                item.habit_name = h['task'] 
                list_view.append(item)
    
    def on_mount(self) -> None:
        # Start focus on the search bar
        self.query_one("#search-input").focus()
        self.refresh_list()

    def on_input_submitted(self) -> None:
        # When you hit Enter in the search bar, jump to the list
        self.query_one("#habit-list").focus()

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        """Triggered when you press Enter on a habit."""
        # 1. Get the name back from the ID
        task_name = event.item.habit_name

        # 2. Update the Data
        data = load_data()
        today = date.today().isoformat()
    
        for h in data.get('habits', []):
            if h['task'] == task_name:
                if today in h['completed_dates']:
                    h['completed_dates'].remove(today)
                    h['streak'] = max(0, h['streak'] - 1)
                else:
                    h['completed_dates'].append(today)
                    h['streak'] += 1
    
        # 3. Save and Refresh
        save_data(data)
        self.refresh_list()
        self.notify(f"Updated '{task_name}'")

    def on_list_view_highlighted(self, event: ListView.Highlighted) -> None:
        """Updates the Main Stage as you move the arrow keys."""
        if event.item:
            task_name = event.item.habit_name
            data = load_data()
        
            # Find the specific habit record (the 'row' in your DS mindset)
            habit = next((h for h in data['habits'] if h['task'] == task_name), None)
        
            if habit:
                # We just update a big string in the details-view
                stats = (
                    f"[bold underline]{habit['task']}[/]\n\n"
                    f"🔥 Current Streak: {habit['streak']} days\n"
                    f"📈 Total Completions: {len(habit['completed_dates'])}\n"
                    f"🆔 ID: {habit['id']}"
                )
                self.query_one("#details-view", Static).update(stats)

if __name__ == "__main__":
    app = HabitApp()
    app.run()