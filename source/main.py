# imports
import os
import tkinter as tk
from tkinter import ttk
from constants import CHARACTER_NAMES, COSTUME_NAMES, BATTLE_STAMP_NAMES, CARD_NAMES, QUEST_NAMES, XP_THRESHOLDS, LEVELS

# Create a reusable function to generate checkbox grids for things like stamps, cards, quests etc.
def create_checkbox_grid(tab, items, items_per_col, num_cols):
    columns = []

    for c in range(num_cols):
        frame = tk.Frame(tab)
        frame.pack(side="left", anchor="n", padx=10)
        columns.append(frame)

    for i, name in enumerate(items):
        col = i // items_per_col
        if col >= num_cols:
            break

        cb = tk.Checkbutton(columns[col], text=name)
        cb.pack(anchor="w")

# tab creation functions
def create_summary_tab(tab):
    label = tk.Label(tab, text="100% Requirements:" \
    "\n\nCollect all 11 Costumes." \
    "\n\nCollect all 24 Battle Stamps." \
    "\n\nCollect all 54 Creepy Treat Cards." \
    "\n\nComplete all required and optional quests." \
    "\n\nAchieve the maximum level (Level 10)")
    label.pack(padx=20, pady=20)

def create_battle_stamps_tab(tab):
    create_checkbox_grid(tab, BATTLE_STAMP_NAMES, 8, 3)

def create_costumes_tab(tab):
    create_checkbox_grid(tab, COSTUME_NAMES, 3, 4)

def create_cards_tab(tab):
    create_checkbox_grid(tab, CARD_NAMES, 9, 4)

def create_level_tab(tab):
    for level in LEVELS:
        checklist = tk.Checkbutton(tab, text=f"Level {level}")
        checklist.pack(anchor="w", padx=10)

def create_quests_tab(tab):
    create_checkbox_grid(tab, QUEST_NAMES, 9, 4)

def main():
    # Create main window
    parent = tk.Tk()
    parent.title("Costume Quest 100% Tracker")
    parent.geometry("800x400")
    parent.minsize(800, 400)

    # Create notebook
    notebook = ttk.Notebook(parent)

    # Create tabs
    tab_summary = ttk.Frame(notebook)
    tab_stamps = ttk.Frame(notebook)
    tab_costumes = ttk.Frame(notebook)
    tab_cards = ttk.Frame(notebook)
    tab_level = ttk.Frame(notebook)
    tab_quests = ttk.Frame(notebook)

    # Add tabs to notebook
    notebook.add(tab_summary, text="Summary")
    notebook.add(tab_stamps, text="Battle Stamps")
    notebook.add(tab_costumes, text="Costumes")
    notebook.add(tab_cards, text="Creepy Treat Cards")
    notebook.add(tab_level, text="Level")
    notebook.add(tab_quests, text="Quests")

    # Create content for each tab
    create_summary_tab(tab_summary)
    create_battle_stamps_tab(tab_stamps)
    create_costumes_tab(tab_costumes)
    create_cards_tab(tab_cards)
    create_level_tab(tab_level)
    create_quests_tab(tab_quests)

    notebook.pack(padx=10, pady=10, fill="both", expand=True)

    # set icon if available
    import constants
    icon_path = os.path.join(constants.BASE_DIR, "icon.ico")
    if os.path.exists(icon_path):
        try:
            parent.iconbitmap(icon_path)
        except Exception:
            pass

    parent.mainloop()

if __name__ == "__main__":
    main()