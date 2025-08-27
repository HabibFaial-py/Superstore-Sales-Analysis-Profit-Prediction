📊 Superstore Sales Analysis & Profit Prediction
📌 Overview

This project performs Exploratory Data Analysis (EDA) and Profit Prediction on the Sample Superstore dataset.
The goal is to uncover sales & profit trends, visualize business insights, and build a simple predictive model using Linear Regression.

🗂 Dataset

The dataset (Sample - Superstore.csv) contains information about customer orders including:

Order details: Order ID, Order Date, Ship Date, Ship Mode

Customer details: Customer ID, Segment, Region, State, City

Transaction details: Sales, Quantity, Discount, Profit

🛠️ Features

✔️ Data Cleaning & Preprocessing (missing values, duplicates, invalid data removal)
✔️ Time-series sales trend analysis
✔️ Visualizations using Matplotlib, Seaborn & Plotly
✔️ Profit vs Discount correlation analysis
✔️ Sales distribution by Region, Segment, and State
✔️ Choropleth Map for sales across USA states
✔️ Linear Regression model for profit prediction

📈 Visualizations

Line Chart: Sales trend over time

Bar Chart: Sales by Segment

Scatter Plot: Discount vs Profit

Pie Chart: Regional sales distribution

Choropleth Map: State-wise sales across the USA

🤖 Machine Learning

A simple Linear Regression model was applied to predict profit from sales:

X (Feature): Sales

y (Target): Profit

The model was trained and predictions were compared against actual profit values.

🖼️ Sample Output
   Sales   Profit   Predicted_Profit
0  261.96   41.91          43.12
1  731.94  219.58         207.44
2   14.62    6.87           5.27
3  957.58 -383.03         272.45
4  22.37    2.51           6.75

🧑‍💻 Tech Stack

Python (Pandas, NumPy, Scikit-learn)

Matplotlib & Seaborn (Data Visualization)

Plotly (Interactive Choropleth Map)

🚀 How to Run

Clone this repository:

git clone https://github.com/HabibFaisal-py/Superstore-Sales-Analysis-Profit-Prediction.git
cd superstore-analysis


Install dependencies:

pip install -r requirements.txt


Run the script:

python superstore_analysis.py

📌 Future Improvements

Add advanced ML models (Random Forest, XGBoost) for better predictions

Build a dashboard using Streamlit/Power BI for real-time analysis

Include customer segmentation using clustering

🙌 Acknowledgments

Dataset: Sample Superstore (Tableau Public / Kaggle)
