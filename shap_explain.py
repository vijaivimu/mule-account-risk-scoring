import pandas as pd
import shap
import joblib
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Load the synthetic dataset
df = pd.read_csv("synthetic_mule_transactions.csv")

# Select features and label
features = [
    "transaction_amount",
    "transaction_frequency",
    "receiver_count",
    "same_day_repeat_txns",
    "avg_transaction_amount"
]
X = df[features]
y = df["is_flagged_fraud"]

# Train/test split (same as model training)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# ✅ Load the pre-trained model
model = joblib.load("fraud_model.pkl")
print("✅ Loaded model from 'fraud_model.pkl'")

# ✅ Initialize SHAP explainer
explainer = shap.Explainer(model, X_train)

# ✅ Compute SHAP values for test set
shap_values = explainer(X_test)

# ✅ Summary bar plot
shap.summary_plot(shap_values, X_test, plot_type="bar", show=False)
plt.tight_layout()
plt.savefig("shap_summary_bar.png")
print("✅ SHAP summary bar plot saved as 'shap_summary_bar.png'")