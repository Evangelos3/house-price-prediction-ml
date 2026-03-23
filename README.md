# Vancouver Real Estate Price Predictor 

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-Machine%20Learning-F7931E.svg)
![Pandas](https://img.shields.io/badge/pandas-data%20analysis-150458.svg)
![Matplotlib](https://img.shields.io/badge/matplotlib-visualization-orange.svg)

## 📖 Overview
This project is a Command-Line Interface (CLI) application built in Python that analyzes historical real estate data from Vancouver. It utilizes data analysis libraries and Machine Learning techniques to track historical price trends and predict future house market prices based on property features.

##  Key Features
The application features an interactive terminal menu with the following capabilities:
1. **Data Loading & Inspection:** Easily load the CSV dataset and view the raw data structure in a tabular format (via Pandas DataFrame).
2. **Historical Price Visualization:** Generates historical line charts using Matplotlib to visualize how real estate prices have fluctuated over time.
3. **Machine Learning Prediction:** Uses a **Linear Regression** algorithm (`scikit-learn`) to predict the expected market price of a property based on its Square Footage and number of Bedrooms. The prediction is also plotted dynamically on the graph.

##  Dataset
This project is designed to work with the **"Vancouver House Prices for past 20 years"** dataset.
* **Source:** [Kaggle Dataset Link](https://www.kaggle.com/datasets/jennyzzhu/vancouver-house-prices-for-past-20-years)

##  Prerequisites & Installation
To run this project locally, you need Python installed on your system along with specific data science libraries.

