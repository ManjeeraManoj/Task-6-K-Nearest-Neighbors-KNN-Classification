# -*- coding: utf-8 -*-
"""Task 6: K-Nearest Neighbors (KNN) Classification.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1loHd1dOqSMwJs-gg19ZL3ht4cE1kFbqx
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from matplotlib.colors import ListedColormap

# 1. Load the data
df = pd.read_csv('/content/Iris.csv')
df.drop(columns='Id', inplace=True)

# 2. Encode target column if needed
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['Species'] = le.fit_transform(df['Species'])

# 3. Split into features and target
X = df.drop('Species', axis=1)
y = df['Species']

# 4. Normalize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 5. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 6. Try different values of K
k_values = list(range(1, 21))
accuracies = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    pred = knn.predict(X_test)
    acc = accuracy_score(y_test, pred)
    accuracies.append(acc)

# 7. Plot K vs Accuracy
plt.figure(figsize=(10,6))
plt.plot(k_values, accuracies, marker='o', linestyle='dashed', color='blue')
plt.title('Accuracy vs K')
plt.xlabel('K')
plt.ylabel('Accuracy')
plt.grid()
plt.show()

# 8. Train final model (e.g., best K)
best_k = k_values[np.argmax(accuracies)]
print("Best K:", best_k)
knn = KNeighborsClassifier(n_neighbors=best_k)
knn.fit(X_train, y_train)

# 9. Evaluate performance
y_pred = knn.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

def plot_decision_boundary(X, y, model, title):
    X = X[:, :2]  # Use only first 2 features
    x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
    y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                         np.arange(y_min, y_max, 0.02))

    model.fit(X, y)
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    plt.figure(figsize=(8, 6))
    cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
    cmap_bold = ['red', 'green', 'blue']

    plt.contourf(xx, yy, Z, cmap=cmap_light)
    for i, color in enumerate(cmap_bold):
        idx = np.where(y == i)
        plt.scatter(X[idx, 0], X[idx, 1], c=color, label=le.inverse_transform([i])[0],
                    edgecolor='black', s=20)
    plt.title(title)
    plt.legend()
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.show()

# Call the function
knn_2d = KNeighborsClassifier(n_neighbors=best_k)
plot_decision_boundary(X_scaled, y, knn_2d, f"KNN (k={best_k}) Decision Boundary (First 2 Features)")