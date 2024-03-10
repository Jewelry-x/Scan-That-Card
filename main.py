from card_search_tool import *
from image_text_extractor import *

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


def select_file():
    global file_path
    file_path = filedialog.askopenfilename()
    if file_path:
        file_label.config(text=f"Selected File: {file_path}")
    else:
        file_label.config(text="No file selected.")


def scan():
    # tree.delete(*tree.get_children())
    card_name = extract(file_path)
    game_id = get_game_id(game_name.get())
    cards = find_card_price(game_id, card_name)

    idx = 0
    for card in cards:

        tree.insert("", "end", text=f"Card {idx}", values=(card[0], card[1], card[2]))
        idx += 1


def main():
    # Create the main window
    root = tk.Tk()
    root.title("Scan that Card!")
    root.geometry("400x300")

    # Define options
    options = [
        "Yu-Gi-Oh!",
        "Magic: the Gathering",
        "Pokémon",
        "Flesh and Blood",
        "Digimon",
    ]

    # Create a variable to store the selected option
    global game_name
    game_name = tk.StringVar(root)
    game_name.set(options[0])  # Set the default selected option

    # Create the dropdown menu
    dropdown = tk.OptionMenu(root, game_name, *options)
    dropdown.pack()

    file_select_button = tk.Button(root, text="Select File", command=select_file)
    file_select_button.pack()

    global file_label
    file_label = tk.Label(root, text="No file selected.")
    file_label.pack()

    scan_button = tk.Button(root, text="Scan the Card!", command=scan)
    scan_button.pack()

    global tree
    tree = ttk.Treeview(root, columns=("Name", "Price", "Condition"), show="headings")

    # Set column headings
    tree.heading("Name", text="Name")
    tree.heading("Price", text="Price")
    tree.heading("Condition", text="Condition")

    # Set column widths
    tree.column("Name", width=200)
    tree.column("Price", width=100)
    tree.column("Condition", width=100)

    # Pack the treeview widget
    tree.pack(expand=True, fill="both")

    # Start the GUI event loop
    root.mainloop()


if __name__ == "__main__":
    main()
    # game_id = get_game_id(game_name)
    # find_card_price(game_id)
