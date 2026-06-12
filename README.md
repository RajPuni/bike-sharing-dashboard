# 🚲 Bike Sharing Demand Analysis Dashboard

An interactive Streamlit dashboard that explores bike rental patterns in Washington D.C. using historical bike-sharing data from 2011–2012.

## 📌 Project Overview

This project analyzes how weather conditions, seasons, working days, and time-related factors influence bike rental demand.

The analysis was completed in three stages:

1. Exploratory Data Analysis (EDA)
2. Data Visualization
3. Interactive Dashboard Development using Streamlit

The final dashboard allows users to interactively explore bike rental trends and gain insights through multiple visualizations and filters.

---

## 📊 Dashboard Features

### Interactive Filters
- Year Selection
- Season Selection
- Weather Category Selection
- Working Day / Non-Working Day Filter

### Visualizations Included
- Monthly Rental Trends
- Hourly Rental Trends
- Seasonal Rental Analysis
- Weather Impact Analysis
- Registered vs Casual Users
- Correlation Heatmap
- Donut Chart Distribution
- Violin Plot Distribution
- Box Plot Analysis
- Peak Rental Hours Analysis

### Dashboard KPIs
- Total Rentals
- Average Hourly Rentals
- Registered Users
- Casual Users

---

## 🗂 Dataset Information

The dataset contains hourly bike rental information from Washington D.C. for the years 2011 and 2012.

### Main Features

| Feature | Description |
|----------|-------------|
| datetime | Hourly timestamp |
| season | Spring, Summer, Fall, Winter |
| holiday | Holiday indicator |
| workingday | Working day indicator |
| weather | Weather condition category |
| temp | Temperature |
| atemp | Feels-like temperature |
| humidity | Relative humidity |
| windspeed | Wind speed |
| casual | Casual user rentals |
| registered | Registered user rentals |
| count | Total rentals |

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Streamlit
- GitHub

---

## 🚀 Running Locally

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

Move into the project folder:

```bash
cd YOUR_REPOSITORY
```

Install required packages:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 🌐 Live Dashboard

Paste your Streamlit dashboard link here: 
https://bike-sharing-dashboard-q7ndnzhbsmgdjesamh8w7u.streamlit.app/



## 📁 Repository Structure

```text
bike-sharing-dashboard/
│
├── app.py
├── traindataset.csv
├── requirements.txt
├── README.md
└── Assignment1_EDA_Updated.ipynb
```

---

## 📈 Key Insights

- Registered users account for the majority of rentals.
- Summer and Fall show the highest bike demand.
- Clear weather conditions result in significantly higher rentals.
- Morning and evening hours exhibit commuting peaks.
- Working days and weekends show distinct rental patterns.

---

## 🎓 Academic Project

This project was developed as part of a Data Analytics/Data Visualization coursework assignment involving:

- Exploratory Data Analysis
- Statistical Visualization
- Dashboard Design
- Cloud Deployment
- GitHub Version Control

Punith LNU

M.Sc. Data Science  
University of Europe for Applied Sciences, Germany
