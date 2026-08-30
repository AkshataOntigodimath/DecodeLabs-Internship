# ============================================================
# Data Classification Using AI - Visualizations
# DecodeLabs Artificial Intelligence Internship - Project 2
# ============================================================

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import ConfusionMatrixDisplay


# Load Iris Dataset
iris = load_iris()

X = iris.data
y = iris.target


# ============================================================
# 1. CLASS DISTRIBUTION GRAPH
# ============================================================

plt.figure(figsize=(8, 5))

plt.bar(
    iris.target_names,
    [list(y).count(0), list(y).count(1), list(y).count(2)]
)

plt.title("Iris Flower Class Distribution")
plt.xlabel("Flower Species")
plt.ylabel("Number of Samples")

plt.tight_layout()
plt.savefig("Task 2/class_distribution.png")

plt.show()


# ============================================================
# 2. TRAIN THE MODEL FOR CONFUSION MATRIX
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)


# ============================================================
# 3. CONFUSION MATRIX VISUALIZATION
# ============================================================

plt.figure(figsize=(7, 5))

ConfusionMatrixDisplay.from_estimator(
    model,
    X_test,
    y_test,
    display_labels=iris.target_names
)

plt.title("Confusion Matrix - Decision Tree Classifier")

plt.tight_layout()
plt.savefig("Task 2/confusion_matrix.png")

plt.show()


print("Visualizations created successfully!")