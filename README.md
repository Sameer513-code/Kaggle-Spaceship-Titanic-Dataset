# Kaggle Spaceship Titanic Dataset

## Objective  
The goal of this project is to build a **machine learning model** that predicts whether a passenger has been transported or not.  

Before implementing models, I followed a structured **machine learning workflow**:  

### Machine Learning Workflow  
1. **Frame the Problem** – Define the objective clearly.  
2. **Gather Data** – Obtain and preprocess the dataset.  
3. **Explore the Data** – Perform data analysis to find patterns.  
4. **Feature Engineering** – Select and transform features to improve performance.  
5. **Train Different Models** – Compare multiple models and select the best ones.  
6. **Fine-tune the Models** – Optimize hyperparameters for better accuracy.  
7. **Evaluate and Compare Performance** – Choose the best-performing model.  
8. **Deploy & Monitor** – Integrate the model into an application if needed.  

---

## Models Implemented  

### Logistic Regression  
**Algorithm:**  
- Its an algorithm that estimates the probability of a binary outcome using the **sigmoid function**, that takes input as independent variables and produces a probability value between 0 and 1. It applies **log-odds transformation** to model relationships between input features and the target variable. 
**Advantages:**  
- Easy to implement when output must be categorical value such as 0 or 1, Yes or no, etc.
- It not only provides a measure of how appropriate a predictor(coefficient size)is, but also its direction of association (positive or negative). 
- Works well on small datasets.  

**Disadvantages:**  
- Assumes a **linear relationship** between features and the target.  

**Hyperparameters Used:**  
```python
solver = 'liblinear'  # Optimization algorithm
C = 1.0  # Regularization strength (smaller = stronger regularization)
```

---

### 2️⃣ KNN
**Algorithm:**  
- KNN uses distance metrics to identify nearest neighbour, operates on the principle of similarity where it predicts the label or value of a new data point by considering the labels or values of its K nearest neighbors in the training dataset. The metrics used are Euclidean, Manhattan and more.

**Advantages:**  
- KNN is simple to implement and understand. 
- Used in many fields, including image recognition, handwriting detection, and video recognition.  

**Disadvantages:**  
- Computationally **expensive**, especially for large datasets.  
- Doesn't perform as well as other complex algorithms like neural networks, decision trees, and support vector machines.  

**Hyperparameters Used:**  
```python
k = 56 #Nearest Neighbour
```

---

### 3️⃣ XGBoost  
**Algorithm:**  
- A gradient boosting model optimized for speed and performance.  

**Advantages:**  
- Handles missing values efficiently.  
- Works well with structured/tabular data.  
- Achieves **high accuracy**.  

**Disadvantages:**  
- Requires careful **hyperparameter tuning**.  
- Can **overfit** if not regularized properly.  

**Hyperparameters Used:**  
```python
learning_rate = 0.1  # Step size at each iteration
n_estimators = 100  # Number of boosting rounds
max_depth = 6  # Maximum depth of a tree
subsample = 0.8  # Fraction of samples used per boosting round
```

---

## Model Performance  
| Model               |  Accuracy  |
|---------------------|------------|
| Logistic Regression | 78%        |
| KNN                 | 79.42%     |
| XGBoost             | 79.84%     |

---

## Improvements  
- **Hyperparameter Optimization** – Use **GridSearchCV** or **RandomizedSearchCV** to find optimal parameters.  
- **Handling Class Imbalance** – Try **SMOTE** or **weighted loss functions** if needed.  

---

### Summary  
Out of three models, **XGBoost model performed the best** with **79.84% accuracy**, making it the most effective for deployment. 🚀  



