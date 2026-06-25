# Import required libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# ------------------------------------------------
# Load the Iris Dataset
# ------------------------------------------------
iris = load_iris()

# Features (Sepal Length, Sepal Width, Petal Length, Petal Width)
X = iris.data

# Target Labels (Flower Types)
y = iris.target

# Print dataset information
print("========== DATASET INFORMATION ==========")
print("Number of Samples :", len(X))
print("Number of Features:", len(X[0]))
print("Target Names      :", iris.target_names)
print()

# ------------------------------------------------
# Split the Dataset
# 80% Training
# 20% Testing
# ------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training Samples :", len(X_train))
print("Testing Samples  :", len(X_test))
print()

# ------------------------------------------------
# Scale the Data
# ------------------------------------------------
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print("Data Scaling Completed.")
print()

# ------------------------------------------------
# Create the KNN Model
# ------------------------------------------------
model = KNeighborsClassifier(n_neighbors=5)

print("KNN Model Created.")
print()

# ------------------------------------------------
# Train the Model
# ------------------------------------------------
model.fit(X_train, y_train)

print("Model Training Completed.")
print()

# ------------------------------------------------
# Predict Test Data
# ------------------------------------------------
y_pred = model.predict(X_test)

print("Prediction Completed.")
print()

# ------------------------------------------------
# Calculate Accuracy
# ------------------------------------------------
accuracy = accuracy_score(y_test, y_pred)

print("========== MODEL ACCURACY ==========")
print(f"Accuracy: {accuracy:.2f}")
print()

# ------------------------------------------------
# Display Confusion Matrix
# ------------------------------------------------
print("========== CONFUSION MATRIX ==========")
cm = confusion_matrix(y_test, y_pred)
print(cm)
print()

# ------------------------------------------------
# Display Classification Report
# ------------------------------------------------
print("========== CLASSIFICATION REPORT ==========")
print(classification_report(
    y_test,
    y_pred,
    target_names=iris.target_names
))

# ------------------------------------------------
# Show Sample Predictions
# ------------------------------------------------
print("========== SAMPLE PREDICTIONS ==========")

for i in range(10):
    actual = iris.target_names[y_test[i]]
    predicted = iris.target_names[y_pred[i]]

    print(f"Sample {i+1}")
    print("Actual    :", actual)
    print("Predicted :", predicted)
    print("---------------------------")