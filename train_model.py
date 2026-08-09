import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix

#load dataset
data_path = 'data/customer_churn_data.csv'
if not os.path.exists(data_path):
    raise FileNotFoundError("Run generate_data.py first to create the dataset.")

df = pd.read_csv(data_path)


#separate features x and target y
X = df[['last_purchase_days_ago', 'total_orders', 'total_spent_usd', 'support_tickets_opened']]
y = df['is_churned']

#train / test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

#train random rorest classifier
model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
model.fit(X_train, y_train)

#model evaluation
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:, 1]

auc_score = roc_auc_score(y_test, y_proba)
print("=== Model Performance ===")
print(f"ROC-AUC Score: {auc_score:.3f}")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

#feature importance extraction
feature_importances = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=True)

#plot feature importances
os.makedirs('reports', exist_ok=True)
plt.figure(figsize=(8, 5))
feature_importances.plot(kind='barh', color='#2b5c8f')
plt.title('Key Drivers of Customer Churn')
plt.xlabel('Relative Importance')
plt.tight_layout()

chart_path = 'reports/churn_feature_importance.png'
plt.savefig(chart_path)
print(f"Feature importance chart saved to {chart_path}")

#generate churn predictions & risk scores for the whole dataset
df['churn_risk_score'] = np.round(model.predict_proba(X)[:, 1] * 100, 1)
df['predicted_churn'] = model.predict(X)

output_path = 'data/customer_churn_scored.csv'
df.to_csv(output_path, index=False)
print(f"Scored dataset saved to {output_path}")