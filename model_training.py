import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

# Load the synthetic dataset
df = pd.read_csv("synthetic_mule_transactions.csv")

# Features to be used for training
features = [
    'transaction_amount',
    'transaction_frequency',
    'receiver_count',
    'same_day_repeat_txns',
    'avg_transaction_amount'
]

# Target label
target = 'is_flagged_fraud'

# Prepare X and y
X = df[features]
y = df[target]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize and train the Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict probabilities on the test set
y_probs = model.predict_proba(X_test)[:, 1]

# Apply threshold of 0.5 to determine fraud flags
y_pred = (y_probs >= 0.5).astype(int)

# Evaluation metrics
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("ROC AUC Score:", roc_auc_score(y_test, y_probs))