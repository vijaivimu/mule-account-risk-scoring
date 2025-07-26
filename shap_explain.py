import pandas as pd
import shap
import joblib
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("synthetic_mule_transactions.csv")

# Feature columns
features = [
    "transaction_amount",
    "transaction_frequency",
    "receiver_count",
    "same_day_repeat_txns",
    "avg_transaction_amount"
]
X = df[features]
y = df["is_flagged_fraud"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Load saved model
model = joblib.load("fraud_model.pkl")

# SHAP TreeExplainer
explainer = shap.Explainer(model, X_train)
shap_values = explainer(X_test)

# ✅ Select only class 1 (fraud) SHAP values
shap_values_class1 = shap_values[..., 1]

# Beeswarm summary plot
shap.plots.beeswarm(shap_values_class1, show=False)
plt.tight_layout()
plt.savefig("shap_beeswarm_summary.png")
print("✅ SHAP beeswarm summary plot saved as 'shap_beeswarm_summary.png'")

# Waterfall plot for one test instance
plt.clf()
shap.plots.waterfall(shap_values_class1[0], show=False)
plt.tight_layout()
plt.savefig("shap_waterfall_txn0.png")
print("✅ SHAP waterfall plot for transaction 0 saved as 'shap_waterfall_txn0.png'")