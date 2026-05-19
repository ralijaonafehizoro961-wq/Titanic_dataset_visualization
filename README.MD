# Titanic Data Analysis

A complete data analysis project on the Titanic dataset using Python and popular data science libraries.


![Titanic](graph/Titanic.jpg)
---

# Project Overview

This project focuses on:
- Data cleaning
- Data exploration
- Survival analysis
- Data visualization
- Correlation analysis

The goal is to better understand the factors that influenced passenger survival on the Titanic.


![GitHub stars](https://img.shields.io/github/stars/ralijaonafehizoro961-wq/Titanic_Dataset_Exploration?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/ralijaonafehizoro961-wq/Titanic_Dataset_Exploration?style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/ralijaonafehizoro961-wq/Titanic_Dataset_Exploration?style=for-the-badge)
---

# Technologies & Libraries

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge)
![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=for-the-badge)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)

---

# 📂 Project Structure
```bash
Titanic_Dataset_Exploration/
│
├── data/
│   └── Titanic-Dataset.csv
│
├── results/
│   └── donnees_nettoyees.csv
│
├── src/
│   ├── Data_exploration/
│   ├── analysis/
│   ├── Missing_data/
|	└── Visualization/
│
├── graph/
│
├── README.md
└── requirements.txt
```

---

# Data Cleaning

The following cleaning tasks were performed:

 Filled missing values in the Age column using the median  
 Filled missing values in the Embarked column using the mode  
 Created a new HasCabin feature  
 Saved the cleaned dataset

---

# Analyses Performed

## 🔹 Survival Rate by Gender

Women had a much higher survival rate than men.

![Gender Survival](graph/rate_comparaison.png)

---

## 🔹 Survival Rate by Passenger Class

First-class passengers had a much higher survival rate than third-class passengers.
![Passenger Class](graph/class_survival.png)

---

## 🔹 Age Distribution of Passengers

Most Titanic passengers were young adults.
![Age Distribution](graph/age_distribution_titanic.png)

---

## 🔹 Survival Distribution

There were more deaths than survivors on the Titanic.
![Survival Distribution](graph/survival_distribution_titanic_pieChart.png)

---

## 🔹 Correlation Heatmap

The heatmap shows relationships between numerical variables such as:
- Passenger class
- Fare
- Survival
- Age

Higher-class passengers and passengers who paid higher fares were more likely to survive.

---

# Visualizations Included

 Bar Charts  
 Pie Charts  
 Histograms  
 Boxplots  
 Heatmaps

---

# Additional Visualizations

## Age Distribution by Survival Status

![Histogram](graph/histogramme_age_survie.png)

---

## Boxplot of Age According to Survival

![Boxplot](graph/boxplot_age_survie.png)

---

# Key Insights

- Women survived more than men
- Wealthier passengers had higher survival chances
- Passenger class strongly influenced survival
- Age had a weaker influence on survival

---

# Learning Objectives

This project helped practice:
- Data cleaning
- Data visualization
- Exploratory Data Analysis (EDA)
- Python programming
- Statistical interpretation

---

# Future Improvements

- Add machine learning models
- Predict passenger survival
- Build interactive dashboards
- Deploy the project online

---

# How to Run the Project

```bash
# clone the repository
git clone https://github.com/ralijaonafehizoro961-wq/Titanic_dataset_visualization.git
cd Titanic_dataset_visualization

# Install the dependence
pip install -r requirements.txt

# Run with this command
# ex : on linux
python3 src/Data_exploration/exp_data_01.py
python3 src/Missing_data/miss_data_01.py

# ex : on Windows
python src/Data_exploration/exp_data_01.py
python src/Missing_data/miss_data_01.py