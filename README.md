This is a professional README.md tailored specifically for your project. It includes the business context, the unified schema explanation, and the progress you have made so far.

Instructions: Create a file named README.md in your root folder and paste the content below.

Ethiopia Financial Inclusion Forecasting System

![alt text](https://img.shields.io/badge/python-3.10+-blue.svg)


![alt text](https://img.shields.io/badge/pandas-2.0+-orange.svg)


![alt text](https://img.shields.io/badge/Status-Interim_Submission_Complete-green.svg)

📌 Project Overview

This project is part of the 10 Academy: AI Mastery - Week 10 Challenge.

Working as a Data Scientist at Selam Analytics, the goal is to build a forecasting system that tracks and predicts Ethiopia's digital financial transformation. We utilize the World Bank’s Global Findex Framework to model two core dimensions:

Access — Account Ownership Rate.

Usage — Digital Payment Adoption Rate.

Ethiopia is currently in a rapid growth phase with the entry of Telebirr and M-Pesa, yet only 49% of adults have a financial account as of 2024. This system helps stakeholders understand what drives inclusion and forecasts trends for 2025–2027.

📂 Project Structure
code
Bash
download
content_copy
expand_less
ethiopia-fi-forecast/
├── data/
│   ├── raw/                  # Original datasets (Unified schema)
│   └── processed/            # Enriched dataset with 2024/2025 proxies
├── notebooks/
│   ├── 01_data_exploration.ipynb   # Task 1: Loading & Enrichment
│   └── 02_exploratory_analysis.ipynb # Task 2: Trend & Event Analysis
├── reports/
│   ├── figures/              # Generated EDA visualizations
│   └── interim_report.md     # Phase I & II Summary Report
├── src/                      # Source code for modeling
├── dashboard/                # Streamlit application (Upcoming)
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
📊 The Unified Data Schema

The project uses a unique "Unified Schema" where all data points (observations, events, and targets) share the same structure:

observation: Measured values (Findex surveys, operator reports).

event: Policies, product launches (e.g., Telebirr Launch, M-Pesa Entry).

target: Official policy goals (e.g., Ethiopia's NFIS-II 60% target).

impact_link: Modeled relationships between events and indicators.

🚀 Key Insights (Phase I & II)

The Access Paradox: Despite 60M+ mobile money registrations, account ownership grew only 3% (46% to 49%) between 2021-2024, suggesting high multi-homing.

P2P Crossover: Digital P2P transfers have officially surpassed ATM cash withdrawals in Ethiopia (Crossover Ratio: 1.08).

Gender Gap: There remains a persistent 19-percentage point gap in account ownership between men and women.

Infrastructure Lead: 4G coverage and Digital ID (Fayda) enrollment are leading indicators for digital payment usage.

🛠️ Installation & Setup

Clone the Repository:

code
Bash
download
content_copy
expand_less
git clone https://github.com/Yodahe2021/ethiopia-fi-forecast
cd ethiopia-fi-forecast

Create Virtual Environment:

code
Bash
download
content_copy
expand_less
python -m venv .venv
# Windows
.venv\Scripts\activate

Install Dependencies:

code
Bash
download
content_copy
expand_less
pip install -r requirements.txt
📅 Roadmap

Task 1: Data Exploration & Enrichment (2025 Proxy Data).

Task 2: Exploratory Data Analysis & Interim Report.

Task 3: Event Impact Modeling (Quantifying "Lift").

Task 4: Forecasting 2025-2027 (Access and Usage).

Task 5: Interactive Dashboard Deployment.

👥 Author

[Your Name] - Data Scientist at Selam Analytics

Project Date: Jan 28 - Feb 03, 2026

Tutors: Kerod, Mahbubah, Filimon

📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
