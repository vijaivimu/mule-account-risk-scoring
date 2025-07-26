# Mule Account Risk Scoring

This repository contains a prototype system for detecting mule accounts using AI-based risk scoring methods. Mule accounts are bank accounts used—knowingly or unknowingly—to facilitate money laundering or fraud by transferring illegally acquired funds.

## 🔍 Objective
To develop a scoring system that evaluates each financial transaction and assigns risk scores at both the transaction and account level. The goal is to preemptively identify suspicious activity and flag potential mule accounts for investigation.

## 🧠 Key Features
- Synthetic transaction data generator
- Risk scoring logic based on behavioral patterns
- Daily risk accumulation per account
- Threshold-based alert mechanism for flagging risky accounts

## 📁 Components
- `data_generator.py` — Creates customizable synthetic transaction datasets
- `risk_scoring.py` — Logic for calculating transaction and account-level scores
- `notebooks/` — Sample Jupyter notebooks for analysis and visualization

## 🛠️ Tech Stack
- Python (Pandas, NumPy, Random)
- Jupyter Notebook (for exploration)
- CSV-based simulation

## 📈 Future Enhancements
- Machine learning-based scoring
- Real-time dashboard
- Integration with simulated banking flows

## 📄 License
This project is for academic and demonstration purposes only.
