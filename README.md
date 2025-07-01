# Task-6-K-Nearest-Neighbors-KNN-Classification

📌 Task Objective

Implement and evaluate the K-Nearest Neighbors (KNN) classifier on a classification dataset, visualize decision boundaries, and answer conceptual interview questions related to KNN.

## ✅ Action Taken

1. Preprocess and load the dataset.
2. Use `StandardScaler` to **Normalize Features**.
3. **Train-Test Split** with an 80-20 ratio.
4. **Train KNN Classifier** with `KNeighborsClassifier` from `sklearn`.
5. **Test for different K values (1-20)** and choose the most accurate K.
6. **Assess the Model** with:
   Confusion Matrix - Accuracy Score
   Report on Classification
7. **Consist of**:
   Plot Accuracy vs. K
   Boundaries for Decisions

   ## 🔍 Results

- **Best K value**: *varies per run, e.g., 6 or 7*
- **Model Accuracy**: *~96% to 100% depending on split*
- **Confusion Matrix**: Shows correct classification for all 3 classes.
- **Decision Boundary**: Visualized in 2D using first 2 features.


## 🛠️ Tools & Libraries

- Python 3
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
