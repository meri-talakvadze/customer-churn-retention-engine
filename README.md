# Customer Churn & Retention Analytics Engine

A customer churn analysis and risk-scoring pipeline built with Python, SQLite, and Power BI. The system processes customer behavioral data, predicts individual churn probabilities using a Random Forest classification model, stores scored output in a relational SQLite database, and presents actionable reporting in Power BI.

---

## Technical Stack & Dependencies

- **Programming:** Python 3.x (`pandas`, `numpy`, `scikit-learn`, `matplotlib`)
- **Database:** SQLite
- **Business Intelligence:** Power BI Desktop, DAX (`CALCULATE`, `DIVIDE`, `SUM`)
- **Version Control:** Git

---

## System Architecture & Workflow

1. **Data Generation (`src/generate_data.py`)**
   Generates customer accounts with behavioral attributes including order history, spending totals, purchase recency, and support ticket counts.

2. **Machine Learning Model (`src/train_model.py`)**
   Trains a Random Forest classifier to predict churn probability (`churn_risk_score`) and assigns binary churn predictions (`predicted_churn`). Generates feature importance charts to highlight key churn drivers.

3. **Database Integration (`src/load_to_sql.py`)**
   Loads the model-scored CSV data into an SQLite database (`data/churn_analytics.db`) under the table `customer_churn_scored`.

4. **SQL Analytics (`queries.sql`)**
   Executes business queries against the SQLite database to extract summary metrics, evaluate support ticket impact, and isolate high-risk accounts.

5. **Power BI Dashboard (`Customer_Churn_Dashboard.pbix`)**
   Connects to the database and utilizes explicit DAX measures to track KPIs, risk distribution, and high-priority accounts for retention outreach.

---

## Key Metrics & Findings

- **Total Analyzed Accounts:** 1,000
- **Overall Churn Rate:** 7.6% (76 churned accounts)
- **Total Revenue at Risk:** $22,910.95
- **Primary Churn Indicator:** Support ticket volume ($\ge 3$ tickets correlates with high churn probability)

---

## Repository Structure

```text
├── data/
│   ├── customer_churn_data.csv
│   ├── customer_churn_scored.csv
│   └── churn_analytics.db
├── reports/
│   └── churn_feature_importance.png
├── src/
│   ├── generate_data.py
│   ├── train_model.py
│   └── load_to_sql.py
├── Customer_Churn_Dashboard.pbix
├── queries.sql
├── .gitignore
└── README.md
