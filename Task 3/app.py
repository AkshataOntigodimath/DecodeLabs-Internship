import tkinter as tk
from tkinter import ttk, messagebox

from recommendation_system import recommend_movies


# -----------------------------
# Functions
# -----------------------------

def get_recommendations():
    selected_genres = []

    for genre, var in genre_vars.items():
        if var.get():
            selected_genres.append(genre)

    if not selected_genres:
        messagebox.showwarning(
            "No Preference Selected",
            "Please select at least one movie genre."
        )
        return

    recommendations = recommend_movies(selected_genres)

    results_text.config(state="normal")
    results_text.delete("1.0", tk.END)

    # User preferences
    results_text.insert(
        tk.END,
        "YOUR MOVIE PREFERENCES\n",
        "heading"
    )
    results_text.insert(
        tk.END,
        "-" * 55 + "\n"
    )
    results_text.insert(
        tk.END,
        "Selected Genres: " + ", ".join(selected_genres) + "\n\n"
    )

    # Recommendations
    results_text.insert(
        tk.END,
        "AI RECOMMENDED MOVIES\n",
        "heading"
    )
    results_text.insert(
        tk.END,
        "-" * 55 + "\n\n"
    )

    if recommendations:
        for index, movie in enumerate(recommendations, start=1):
            results_text.insert(
                tk.END,
                f"{index}. {movie['name']}\n",
                "movie"
            )

            results_text.insert(
                tk.END,
                f"   Genres: {', '.join(movie['genres'])}\n"
            )

            results_text.insert(
                tk.END,
                f"   Match Score: {movie['score']}\n\n",
                "score"
            )
    else:
        results_text.insert(
            tk.END,
            "No recommendations found for your selected genres."
        )

    results_text.config(state="disabled")


def clear_selection():
    for var in genre_vars.values():
        var.set(False)

    results_text.config(state="normal")
    results_text.delete("1.0", tk.END)

    results_text.insert(
        tk.END,
        "Select your preferred genres above and click\n"
        "'Get Recommendations' to discover movies.",
        "info"
    )

    results_text.config(state="disabled")


# -----------------------------
# Main Window
# -----------------------------

root = tk.Tk()

root.title("AI Movie Recommendation System")
root.geometry("760x720")
root.resizable(False, False)


# -----------------------------
# Styling
# -----------------------------

style = ttk.Style()

style.configure(
    "Title.TLabel",
    font=("Arial", 22, "bold")
)

style.configure(
    "Subtitle.TLabel",
    font=("Arial", 11)
)

style.configure(
    "TButton",
    font=("Arial", 10, "bold"),
    padding=8
)

style.configure(
    "TCheckbutton",
    font=("Arial", 10)
)

style.configure(
    "TLabelframe.Label",
    font=("Arial", 11, "bold")
)


# -----------------------------
# Header
# -----------------------------

header_frame = tk.Frame(root)
header_frame.pack(pady=18)

title_label = ttk.Label(
    header_frame,
    text="🎬 AI Movie Recommendation System",
    style="Title.TLabel"
)
title_label.pack()

subtitle_label = ttk.Label(
    header_frame,
    text="Select your favorite genres and discover movies based on your preferences.",
    style="Subtitle.TLabel"
)
subtitle_label.pack(pady=6)


# -----------------------------
# Genre Selection
# -----------------------------

genre_frame = ttk.LabelFrame(
    root,
    text="  Select Your Preferred Genres  ",
    padding=18
)

genre_frame.pack(
    padx=30,
    pady=10,
    fill="x"
)


genres = [
    "Action",
    "Adventure",
    "Animation",
    "Comedy",
    "Crime",
    "Drama",
    "Horror",
    "Romance",
    "Sci-Fi",
    "Thriller"
]

genre_vars = {}

for index, genre in enumerate(genres):

    var = tk.BooleanVar(value=False)

    genre_vars[genre] = var

    checkbox = ttk.Checkbutton(
        genre_frame,
        text=genre,
        variable=var
    )

    row = index // 2
    column = index % 2

    checkbox.grid(
        row=row,
        column=column,
        padx=50,
        pady=7,
        sticky="w"
    )


# -----------------------------
# Buttons
# -----------------------------

button_frame = tk.Frame(root)
button_frame.pack(pady=12)

recommend_button = ttk.Button(
    button_frame,
    text="★  Get Recommendations",
    command=get_recommendations
)

recommend_button.grid(
    row=0,
    column=0,
    padx=10
)

clear_button = ttk.Button(
    button_frame,
    text="↻  Clear",
    command=clear_selection
)

clear_button.grid(
    row=0,
    column=1,
    padx=10
)


# -----------------------------
# Results
# -----------------------------

results_frame = ttk.LabelFrame(
    root,
    text="  Recommendation Results  ",
    padding=12
)

results_frame.pack(
    padx=30,
    pady=8,
    fill="both",
    expand=True
)


results_text = tk.Text(
    results_frame,
    height=18,
    width=80,
    font=("Arial", 10),
    wrap="word",
    padx=12,
    pady=12,
    state="disabled"
)

results_text.pack(
    side="left",
    fill="both",
    expand=True
)


scrollbar = ttk.Scrollbar(
    results_frame,
    orient="vertical",
    command=results_text.yview
)

scrollbar.pack(
    side="right",
    fill="y"
)

results_text.config(
    yscrollcommand=scrollbar.set
)


# -----------------------------
# Text Formatting
# -----------------------------

results_text.tag_configure(
    "heading",
    font=("Arial", 12, "bold")
)

results_text.tag_configure(
    "movie",
    font=("Arial", 11, "bold")
)

results_text.tag_configure(
    "score",
    font=("Arial", 10, "bold")
)

results_text.tag_configure(
    "info",
    font=("Arial", 11)
)


# Initial message

results_text.config(state="normal")

results_text.insert(
    tk.END,
    "Select your preferred genres above and click\n"
    "'Get Recommendations' to discover movies.",
    "info"
)

results_text.config(state="disabled")


# -----------------------------
# Run Application
# -----------------------------

root.mainloop()