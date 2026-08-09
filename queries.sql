-- Calculates total customers, churn count, churn rate %, and total revenue at risk.
SELECT 
    COUNT(customer_id) AS total_customers,
    SUM(CASE WHEN is_churned = 1 THEN 1 ELSE 0 END) AS total_churned_customers,
    ROUND(CAST(SUM(CASE WHEN is_churned = 1 THEN 1 ELSE 0 END) AS FLOAT) / COUNT(customer_id) * 100, 2) AS churn_rate_pct,
    ROUND(SUM(CASE WHEN is_churned = 1 THEN total_spent_usd ELSE 0 END), 2) AS total_revenue_at_risk_usd
FROM customer_churn_scored;

-- Evaluates how support ticket volume correlates with actual churn and predicted risk scores.
SELECT 
    support_tickets_opened,
    COUNT(customer_id) AS total_customers,
    SUM(is_churned) AS churned_customers,
    ROUND(CAST(SUM(is_churned) AS FLOAT) / COUNT(customer_id) * 100, 2) AS group_churn_rate_pct,
    ROUND(AVG(churn_risk_score), 2) AS avg_churn_risk_score
FROM customer_churn_scored
GROUP BY support_tickets_opened
ORDER BY support_tickets_opened ASC;

-- Breaks down average spend and last purchase recency between retained vs. churned customers.
SELECT 
    is_churned,
    COUNT(customer_id) AS customer_count,
    ROUND(AVG(total_spent_usd), 2) AS avg_customer_spend_usd,
    ROUND(AVG(last_purchase_days_ago), 1) AS avg_days_since_last_purchase,
    ROUND(AVG(total_orders), 1) AS avg_total_orders
FROM customer_churn_scored
GROUP BY is_churned;
-- Filters for accounts with a Machine Learning risk score >= 70% to prioritize customer success outreach.
SELECT 
    customer_id,
    total_spent_usd,
    support_tickets_opened,
    last_purchase_days_ago,
    churn_risk_score
FROM customer_churn_scored
WHERE churn_risk_score >= 70.0
ORDER BY churn_risk_score DESC, total_spent_usd DESC;