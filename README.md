# 🎓 Student Resource & Attendance Analytics Dashboard

A professional data analytics dashboard built entirely using **Python** and **Basic SQL (SQLite)** via the **Cursor AI Code Editor**. This project visualizes real-time metrics for student registration counts, department-wise average attendance rates, and tracking metrics for top downloaded study resources.

## 🚀 Features
- **Core KPI Metrics Grid:** Dynamic calculation cards tracking Total Registered Students, Average Class Attendance %, and Top Utilized Resource.
- **Dynamic Branch Filtering:** Sidebar selector to drill down analytical parameters across individual departments dynamically.
- **Interactive Visualizations:** Sleek Streamlit chart views tracking Present vs Absent distributions.

## 🛠️ Tech Stack & Frameworks
- **Language:** Python 3.x
- **Database Engine:** SQLite3 (Native Python Database)
- **Frontend Dashboard App:** Streamlit Layer
- **Data Processing Engine:** Pandas DataFrame Matrices

## 📁 Repository Structure
- `app.py` - Core Streamlit frontend layout interface and rendering logic pipelines.
- `database.py` - Core schema architecture script initializing the relational `college.db` database layer.
- `requirements.txt` - Python environment setup components metadata configurations.
- `.gitignore` - Security path filter hiding local databases from public tracking.

## 💻 Local Setup & Execution Guide

Follow these sequential parameters within your developer terminal interface workspace setup environment:

### 1. Re-initialize Dependency Packages Stack
```bash
pip install -r requirements.txt
```

### 2. Configure Local Structured Database Snapshot Schema
```bash
python database.py
```

### 3. Bootstrap Local Server Runtime Operations
```bash
python -m streamlit run app.py
```
*Your interactive analytical visual dashboard template will automatically load onto your native default network channel layer at: `http://localhost:8501`*

---
*Built with precision using Cursor IDE toolsets framework compliance.*
