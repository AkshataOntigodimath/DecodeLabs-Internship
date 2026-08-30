🤖 AI Flower Classification

📌 Project Overview

AI Flower Classification is a machine learning project that uses the Iris Dataset to classify flowers into three different species based on their physical measurements.

The project uses a Decision Tree Classifier and provides a simple graphical user interface (GUI) where users can enter flower measurements and receive an AI-based prediction.

---

🌸 Flower Classes

The model classifies flowers into:

- 🌸 Setosa
- 🌼 Versicolor
- 🌺 Virginica

---

🧠 Machine Learning Model

Algorithm: Decision Tree Classifier

The model is trained using the Iris dataset and learns patterns from four flower measurements:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

The dataset is divided into training and testing data before training the model.

---

📊 Dataset

Dataset: Iris Dataset

Information| Details
Total Samples| 150
Features| 4
Classes| 3
Test Size| 20%
Algorithm| Decision Tree Classifier

---

🖥️ GUI Application

The project includes a Tkinter-based graphical interface.

Users can enter the four flower measurements and click:

🔍 Predict Flower

The application then displays the predicted flower species.

The GUI also includes:

📊 View Model Results

This displays the model accuracy, dataset information, class distribution graph, and confusion matrix.

---

📈 Visualizations

The project includes two important visualizations:

Class Distribution

Shows the distribution of the three flower classes in the dataset.

Confusion Matrix

Shows how accurately the trained model classified the flowers across the three classes.

---

🛠️ Technologies Used

- Python
- Scikit-learn
- Tkinter
- Pillow
- Matplotlib
- Pandas
- Git & GitHub

---

📂 Project Structure

Task 2
│
├── classification.py
├── visualizations.py
├── app.py
├── class_distribution.png
├── confusion_matrix.png
└── README.md

---

▶️ How to Run

1. Open the project in VS Code

Open the main project folder:

Decodelabs_AI_Project1

2. Install required libraries

Run:

pip install scikit-learn matplotlib pandas pillow

3. Run the classification program

python "Task 2/classification.py"

4. Run the GUI application

python "Task 2/app.py"

The AI Flower Classification window will open.

---

🎯 Project Features

✅ Iris dataset classification

✅ Decision Tree machine learning model

✅ Train-test dataset splitting

✅ Model accuracy calculation

✅ Flower prediction through GUI

✅ Separate professional GUI window

✅ Class distribution visualization

✅ Confusion matrix visualization

✅ Model performance window

---

🚀 Project Outcome

This project demonstrates the complete basic machine learning workflow:

Dataset → Data Splitting → Model Training → Prediction → Evaluation → Visualization → GUI Application

It combines machine learning concepts with a user-friendly desktop application.