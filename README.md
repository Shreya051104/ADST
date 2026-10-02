# 💊 PharmaOptima: Pharmaceutical Market Intelligence & Sales Analytics

[![Python](https://img.shields.io/badge/Python-3.14-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-orange.svg)](https://pandas.pydata.org/)
[![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow.svg)](https://powerbi.microsoft.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An advanced data science and exploratory data analysis (EDA) framework built for multi-regional pharmaceutical market intelligence, drug pricing strategy optimization, and commercial performance tracking.

---

## 👨‍💻 Project Authors & Evaluation
* **Developer / Student:** Shreya Tripathi (Master of Computer Applications - MCA)
* **Evaluator / Professor:** Prof. Durga Bravish

---

## 📂 Project Overview
**PharmaOptima** is an academic data science laboratory project designed to ingest, clean, analyze, and visualize a multi-regional pharmaceutical dataset comprising **1,500 monthly market records** across **22 commercial, clinical, and competitive attributes**. 

The pipeline combines robust Python-based statistical analysis (`pandas`, `numpy`, `matplotlib`, `seaborn`) with interactive business intelligence dashboarding via **Microsoft Power BI** to uncover key revenue drivers, regional sales distribution, and pricing elasticity.

---

## 📊 Key Findings & Insights
* **Pricing Impact on Revenue:** Correlation analysis revealed a near-perfect positive correlation ($r = 0.988$) between `drug_price` and `total_revenue`, establishing pricing strategy as the primary top-line revenue driver.
* **Top Therapeutic Areas:** **Neurology** generated the highest total revenue ($11.33M), closely followed by **Diabetes** ($10.18M).
* **Regional Performance:** **Europe** led global markets with $21.09M in total revenue, followed closely by **North America** ($19.67M).
* **Data Quality:** Automated missing value audits confirmed **0 missing values** across all 22 features, ensuring absolute dataset integrity.

---

## 🛠️ Tech Stack & Libraries
* **Programming Language:** Python
* **Data Manipulation & Analysis:** `pandas`, `numpy`
* **Data Visualization:** `matplotlib`, `seaborn`
* **Business Intelligence:** Microsoft Power BI (`.pbit` / `.pbix`)
* **Environment:** Jupyter Notebook / Visual Studio Code

---

## 🗂️ Dataset Schema (`pharma_dataset.csv`)
The dataset spans 22 distinct features categorized into:
1. **Identifiers & Categoricals:** `drug_id`, `drug_name`, `therapeutic_area`, `molecule_type` (*Small Molecule, Biologic, Biosimilar*), `region`, `hospital_tier`, `patient_income_level`.
2. **Numerical & Financial Metrics:** `launch_year`, `units_sold`, `drug_price`, competitor prices (`competitor_1_price` to `3`), `insurance_coverage`, `doctor_visits`, `marketing_spend`, `rep_visits`, `regulatory_flags`, `adverse_events`, `total_revenue`, `market_share`.

---

## 🚀 Getting Started & Installation

To run the data analysis pipeline locally:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/PharmaOptima.git](https://github.com/your-username/PharmaOptima.git)
   cd PharmaOptima
