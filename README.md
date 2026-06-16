# AI_Dataset_Explorer

# 📊 AI Dataset Explorer

An interactive, modular **Automated Exploratory Data Analysis (EDA)** and Data Visualization web application built using Python and Streamlit. This application acts as a "Mini Data Scientist," helping users upload any CSV dataset, instantly analyze its properties, discover outliers, visualize distributions, and generate high-level data insights.

## 🚀 Live Demo
🔗 **[Paste your live Streamlit App URL here]**

---

## ✨ Features

* **🗂️ Smart Data Loading:** Instantly view dataset previews, total rows/columns, memory usage tracking, and a global missing value counter.
* **📈 Automated EDA Dashboard:**
  * Comprehensive breakdown of column data types.
  * Exact counts and percentages of missing values per column.
  * Statistical summaries for both numeric (`describe()`) and categorical features.
* **🚨 Outlier Detection:** Automated calculation using the Interquartile Range (IQR) method to count exactly how many outliers reside in each numerical feature.
* **🎨 Dynamic Data Visualizations:** Fully interactive charts powered by Plotly:
  * Histograms & Box plots for individual numerical distributions.
  * Scatter plots & Annotated Correlation Heatmaps for bivariate analysis.
  * Interactive Pie Charts for categorical slice breakdowns.
* **🤖 AI-Powered Insights:** Integrated with large language models to deliver structured dataset overviews, data quality warnings, and actionable machine learning advice.

---

## 📂 Project Architecture

The codebase follows a clean, modular, and object-oriented structure for optimal maintainability:

```text
├── app.py                 # Main Streamlit web application interface & layout
├── data_loader.py         # Handles CSV reading and structural memory computation
├── eda.py                 # Core business logic for statistical summaries and IQR outliers
├── visualizer.py          # Generates all interactive Plotly plots and heatmaps
├── ai_insights.py         # Interfaces with LLM APIs to generate analytical summaries
└── requirements.txt       # Production and local development dependencies
