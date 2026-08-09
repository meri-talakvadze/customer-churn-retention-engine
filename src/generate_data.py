import pandas as pd
import numpy as np
from datetime import datetime, timedelta

#setting seed for reproducible data
np.random.seed(42)

n_customers = 1000
start_date = datetime(2025, 1, 1)

customer_ids = [f"CUST-{1000 + i}" for i in range(n_customers)]

#generating realistic customer attributes
recency_days = np.random.exponential(scale=45, size=n_customers).astype(int)
recency_days = np.clip(recency_days, 1, 365)

frequency = np.random.negative_binomial(n=3, p=0.2, size=n_customers) + 1
monetary_per_order = np.random.gamma(shape=3, scale=25, size=n_customers)
total_monetary = np.round(frequency * monetary_per_order, 2)

support_tickets = np.random.poisson(lam=1.5, size=n_customers)

#defining churn condition: high inactivity or low purchases with high support tickets
churn_prob = 1 / (1 + np.exp(-(-2 + 0.02 * recency_days + 0.4 * support_tickets - 0.005 * total_monetary)))
churned = (np.random.rand(n_customers) < churn_prob).astype(int)

df = pd.DataFrame({
    'customer_id': customer_ids,
    'last_purchase_days_ago': recency_days,
    'total_orders': frequency,
    'total_spent_usd': total_monetary,
    'support_tickets_opened': support_tickets,
    'is_churned': churned
})

#saving to data folder
df.to_csv('data/customer_churn_data.csv', index=False)
print("Dataset created successfully in data/customer_churn_data.csv")
