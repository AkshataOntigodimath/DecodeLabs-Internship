# ============================================================
# Data Classification Using AI
# DecodeLabs Artificial Intelligence Internship - Project 2
# ============================================================

# Import required libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pandas as pd


print("=" * 60)
print("       DATA CLASSIFICATION USING ARTIFICIAL INTELLIGENCE")
print("=" * 60)


# ------------------------------------------------------------
# 1. LOAD THE DATASET
# ------------------------------------------------------------

iris = load_iris()

# Create a DataFrame for better dataset analysis
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = iris.target

print("\n1. DATASET INFORMATION")
print("-" * 60)

print("Dataset Name: Iris Flower Dataset")
print("Number of Samples:", df.shape[0])
print("Number of Features:", len(iris.feature_names))

print("\nFeatures:")
for feature in iris.feature_names:
    print("-", feature)

print("\nClasses:")
for index, species in enumerate(iris.target_names):
    print(f"{index} - {species}")


# ------------------------------------------------------------
# 2. DISPLAY SAMPLE DATA
# ------------------------------------------------------------

print("\n2. SAMPLE DATA")
print("-" * 60)

print(df.head())


# ------------------------------------------------------------
# 3. PREPARE FEATURES AND TARGET
# ------------------------------------------------------------

X = iris.data
y = iris.target


# ------------------------------------------------------------
# 4. SPLIT DATA INTO TRAINING AND TESTING SETS
# ------------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\n3. DATA SPLITTING")
print("-" * 60)

print("Training Samples:", len(X_train))
print("Testing Samples:", len(X_test))


# ------------------------------------------------------------
# 5. CREATE AND TRAIN THE AI MODEL
# ------------------------------------------------------------

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)

print("\n4. MODEL TRAINING")
print("-" * 60)

print("Algorithm Used: Decision Tree Classifier")
print("Model training completed successfully!")


# ------------------------------------------------------------
# 6. MAKE PREDICTIONS
# ------------------------------------------------------------

y_pred = model.predict(X_test)


# ------------------------------------------------------------
# 7. MODEL EVALUATION
# ------------------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\n5. MODEL EVALUATION")
print("-" * 60)

print(f"Model Accuracy: {accuracy * 100:.2f}%")


# Classification Report
print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    target_names=iris.target_names
))


# Confusion Matrix
print("Confusion Matrix:")

cm = confusion_matrix(y_test, y_pred)
print(cm)


# ------------------------------------------------------------
# 8. MAKE A NEW PREDICTION
# ------------------------------------------------------------

print("\n6. NEW DATA PREDICTION")
print("-" * 60)

# Example flower measurements
new_flower = [[5.1, 3.5, 1.4, 0.2]]

prediction = model.predict(new_flower)

predicted_species = iris.target_names[prediction[0]]

print("Input Values:", new_flower[0])
print("Predicted Flower Species:", predicted_species)


print("\n" + "=" * 60)
print("PROJECT EXECUTION COMPLETED SUCCESSFULLY!")
print("=" * 60)