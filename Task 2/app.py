import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


# ============================================================
# LOAD IRIS DATASET
# ============================================================

iris = load_iris()

X = iris.data
y = iris.target


# ============================================================
# SPLIT DATASET
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ============================================================
# TRAIN MACHINE LEARNING MODEL
# ============================================================

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)


# ============================================================
# CALCULATE MODEL ACCURACY
# ============================================================

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)


# ============================================================
# GUI FUNCTIONS
# ============================================================

def show_results():

    results_window = tk.Toplevel(root)

    results_window.title("Model Results")

    results_window.geometry("900x700")

    results_window.resizable(False, False)

    results_window.configure(bg="#f4f7fb")


    # ---------------- TITLE ----------------

    title = tk.Label(
        results_window,
        text="📊 Model Performance",
        font=("Arial", 22, "bold"),
        bg="#f4f7fb",
        fg="#1f4e79"
    )

    title.pack(pady=(20, 10))


    # ---------------- MODEL INFORMATION ----------------

    info = tk.Label(
        results_window,
        text=(
            f"Model: Decision Tree Classifier    |    "
            f"Accuracy: {accuracy * 100:.2f}%"
        ),
        font=("Arial", 13, "bold"),
        bg="#f4f7fb",
        fg="#333333"
    )

    info.pack(pady=5)


    # ---------------- DATASET INFORMATION ----------------

    dataset_info = tk.Label(
        results_window,
        text="Dataset: Iris Dataset  •  Samples: 150  •  Features: 4  •  Classes: 3",
        font=("Arial", 11),
        bg="#f4f7fb",
        fg="#555555"
    )

    dataset_info.pack(pady=(0, 15))


    # ---------------- GRAPH CONTAINER ----------------

    graph_frame = tk.Frame(
        results_window,
        bg="#f4f7fb"
    )

    graph_frame.pack(pady=5)


    # ========================================================
    # CLASS DISTRIBUTION GRAPH
    # ========================================================

    try:

        distribution_image = Image.open(
            "Task 2/class_distribution.png"
        )

        distribution_image.thumbnail(
            (380, 330)
        )

        distribution_photo = ImageTk.PhotoImage(
            distribution_image
        )

        distribution_title = tk.Label(
            graph_frame,
            text="Class Distribution",
            font=("Arial", 12, "bold"),
            bg="#f4f7fb",
            fg="#333333"
        )

        distribution_title.grid(
            row=0,
            column=0,
            pady=(0, 5)
        )

        distribution_label = tk.Label(
            graph_frame,
            image=distribution_photo,
            bg="white",
            bd=1,
            relief="solid"
        )

        distribution_label.grid(
            row=1,
            column=0,
            padx=15
        )

        # Keep image in memory
        distribution_label.image = distribution_photo


    except FileNotFoundError:

        distribution_error = tk.Label(
            graph_frame,
            text="class_distribution.png not found.",
            font=("Arial", 11),
            bg="#f4f7fb",
            fg="red"
        )

        distribution_error.grid(
            row=1,
            column=0,
            padx=15
        )


    # ========================================================
    # CONFUSION MATRIX GRAPH
    # ========================================================

    try:

        confusion_image = Image.open(
            "Task 2/confusion_matrix.png"
        )

        confusion_image.thumbnail(
            (380, 330)
        )

        confusion_photo = ImageTk.PhotoImage(
            confusion_image
        )

        confusion_title = tk.Label(
            graph_frame,
            text="Confusion Matrix",
            font=("Arial", 12, "bold"),
            bg="#f4f7fb",
            fg="#333333"
        )

        confusion_title.grid(
            row=0,
            column=1,
            pady=(0, 5)
        )

        confusion_label = tk.Label(
            graph_frame,
            image=confusion_photo,
            bg="white",
            bd=1,
            relief="solid"
        )

        confusion_label.grid(
            row=1,
            column=1,
            padx=15
        )

        # Keep image in memory
        confusion_label.image = confusion_photo


    except FileNotFoundError:

        confusion_error = tk.Label(
            graph_frame,
            text="confusion_matrix.png not found.",
            font=("Arial", 11),
            bg="#f4f7fb",
            fg="red"
        )

        confusion_error.grid(
            row=1,
            column=1,
            padx=15
        )


    # ---------------- CLOSE BUTTON ----------------

    close_button = tk.Button(
        results_window,
        text="Close",
        command=results_window.destroy,
        font=("Arial", 11, "bold"),
        padx=30,
        pady=8,
        cursor="hand2"
    )

    close_button.pack(
        pady=20
    )


# ============================================================
# PREDICT FLOWER
# ============================================================

def predict_flower():

    try:

        sepal_length = float(
            sepal_length_entry.get()
        )

        sepal_width = float(
            sepal_width_entry.get()
        )

        petal_length = float(
            petal_length_entry.get()
        )

        petal_width = float(
            petal_width_entry.get()
        )


        prediction = model.predict([[
            sepal_length,
            sepal_width,
            petal_length,
            petal_width
        ]])


        flower_name = iris.target_names[
            prediction[0]
        ]


        result_label.config(
            text=f"🌸 Predicted Flower: {flower_name.title()}"
        )


    except ValueError:

        messagebox.showerror(
            "Invalid Input",
            "Please enter valid numerical values."
        )


# ============================================================
# CLEAR INPUT FIELDS
# ============================================================

def clear_fields():

    sepal_length_entry.delete(
        0,
        tk.END
    )

    sepal_width_entry.delete(
        0,
        tk.END
    )

    petal_length_entry.delete(
        0,
        tk.END
    )

    petal_width_entry.delete(
        0,
        tk.END
    )


    result_label.config(
        text="Prediction will appear here"
    )


# ============================================================
# MAIN APPLICATION WINDOW
# ============================================================

root = tk.Tk()

root.title("AI Flower Classification")

root.geometry("650x650")

root.resizable(False, False)

root.configure(
    bg="#f4f7fb"
)


# ============================================================
# HEADER
# ============================================================

header = tk.Frame(
    root,
    bg="#1f4e79",
    height=100
)

header.pack(
    fill="x"
)


title_label = tk.Label(
    header,
    text="🌸 AI Flower Classification",
    font=("Arial", 24, "bold"),
    bg="#1f4e79",
    fg="white"
)

title_label.pack(
    pady=(20, 5)
)


subtitle_label = tk.Label(
    header,
    text="Machine Learning Prediction using Iris Dataset",
    font=("Arial", 11),
    bg="#1f4e79",
    fg="white"
)

subtitle_label.pack()


# ============================================================
# INPUT SECTION
# ============================================================

content = tk.Frame(
    root,
    bg="#f4f7fb"
)

content.pack(
    pady=25
)


info_label = tk.Label(
    content,
    text="Enter Flower Measurements",
    font=("Arial", 16, "bold"),
    bg="#f4f7fb",
    fg="#1f2937"
)

info_label.grid(
    row=0,
    column=0,
    columnspan=2,
    pady=(0, 20)
)


# ============================================================
# INPUT FIELDS
# ============================================================

labels = [
    "Sepal Length (cm)",
    "Sepal Width (cm)",
    "Petal Length (cm)",
    "Petal Width (cm)"
]


entries = []


for i, label_text in enumerate(labels):

    label = tk.Label(
        content,
        text=label_text,
        font=("Arial", 12),
        bg="#f4f7fb"
    )

    label.grid(
        row=i + 1,
        column=0,
        sticky="w",
        padx=20,
        pady=8
    )


    entry = ttk.Entry(
        content,
        width=30
    )

    entry.grid(
        row=i + 1,
        column=1,
        padx=20,
        pady=8
    )


    entries.append(entry)


sepal_length_entry = entries[0]

sepal_width_entry = entries[1]

petal_length_entry = entries[2]

petal_width_entry = entries[3]


# ============================================================
# BUTTONS
# ============================================================

button_frame = tk.Frame(
    root,
    bg="#f4f7fb"
)

button_frame.pack(
    pady=20
)


predict_button = tk.Button(
    button_frame,
    text="🔍 Predict Flower",
    command=predict_flower,
    font=("Arial", 12, "bold"),
    bg="#1f4e79",
    fg="white",
    padx=20,
    pady=10,
    cursor="hand2"
)

predict_button.grid(
    row=0,
    column=0,
    padx=10
)


clear_button = tk.Button(
    button_frame,
    text="Clear",
    command=clear_fields,
    font=("Arial", 12),
    padx=25,
    pady=10,
    cursor="hand2"
)

clear_button.grid(
    row=0,
    column=1,
    padx=10
)


# ============================================================
# PREDICTION RESULT
# ============================================================

result_frame = tk.Frame(
    root,
    bg="white",
    bd=1,
    relief="solid"
)

result_frame.pack(
    padx=60,
    pady=10,
    fill="x"
)


result_label = tk.Label(
    result_frame,
    text="Prediction will appear here",
    font=("Arial", 17, "bold"),
    bg="white",
    fg="#1f4e79",
    pady=25
)

result_label.pack()


# ============================================================
# MODEL RESULTS BUTTON
# ============================================================

results_button = tk.Button(
    root,
    text="📊 View Model Results",
    command=show_results,
    font=("Arial", 11, "bold"),
    bg="#2e7d32",
    fg="white",
    padx=20,
    pady=8,
    cursor="hand2"
)

results_button.pack(
    pady=5
)


# ============================================================
# MODEL INFORMATION
# ============================================================

accuracy_label = tk.Label(
    root,
    text=(
        f"Model: Decision Tree Classifier   |   "
        f"Accuracy: {accuracy * 100:.2f}%"
    ),
    font=("Arial", 11),
    bg="#f4f7fb",
    fg="#555555"
)

accuracy_label.pack(
    pady=15
)


# ============================================================
# FOOTER
# ============================================================

footer = tk.Label(
    root,
    text="AI Classification Project • Iris Dataset",
    font=("Arial", 9),
    bg="#f4f7fb",
    fg="#777777"
)

footer.pack(
    side="bottom",
    pady=15
)


# ============================================================
# START APPLICATION
# ============================================================

root.mainloop()