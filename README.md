
# AI Air Quality Project - Health Risk Predictor
## Overview
This project implements a machine learning model to predict health risk scores based on air quality and environmental parameters. Using a Random Forest Regressor, the system analyzes nine key environmental features to estimate a health risk score, providing valuable insights for public health monitoring and environmental assessment.

## Features
Data Processing: Automatic handling of missing values using mean imputation

Machine Learning Model: Random Forest Regressor with 100 decision trees

Evaluation Metrics: Mean Absolute Error (MAE) and R-squared (R²) score

Feature Set: 9 environmental parameters including PM2.5, NO2, CO2, humidity, temperature, pressure, wind gust, visibility, and UV index

# Features Used
Feature	Description
pm2.5	Particulate matter 2.5 concentration
no2	Nitrogen dioxide levels
co2	Carbon dioxide concentration
humidity	Relative humidity percentage
temp	Temperature reading
pressure	Atmospheric pressure
windgust	Wind gust speed
visibility	Visibility distance
uvindex	UV radiation index
Installation
Prerequisites
Python 3.7 or higher

pip package manager

# Required Packages
bash
pip install pandas scikit-learn openpyxl
# Usage
Ensure your dataset is in Excel format named DQN1 Dataset.xlsx with a sheet named 'Data'

The dataset should contain the feature columns listed above and a 'healthRiskScore' column

Run the script:

bash
python predict_health_risk.py
# Expected Output
The script will output the model's performance metrics:

Mean Absolute Error (MAE): Average prediction error in health risk score units

R-squared (R²): Coefficient of determination indicating model fit (0-1, closer to 1 is better)

# Data Requirements
The Excel file must contain all feature columns and the target column

Columns are case-sensitive (use exact names as listed in features table)

The script automatically handles missing values by using column means

# Model Training
Training/Testing Split: 80/20 ratio

Random State: 42 (for reproducibility)

Number of Trees: 100

Algorithm: Random Forest Regression

# Performance Metrics
The model uses two primary evaluation metrics:

MAE: Measures average absolute difference between predicted and actual values

R² Score: Indicates the proportion of variance in the dependent variable that's predictable from the independent variables

# Project Structure
text
ai-airquality-project/
├── predict_health_risk.py    # Main script
├── DQN1 Dataset.xlsx         # Dataset file (required)
├── README.md                 # Project documentation
└── requirements.txt          # Dependencies (optional)
# Future Improvements
Hyperparameter tuning for optimized model performance

Cross-validation implementation

Feature importance analysis

Visualization of predictions vs actual values

Support for multiple data formats (CSV, JSON)

API endpoint integration for real-time predictions

Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

License
This project is part of the WGU GitLab environment for student repositories.

Author
JWillD682 - WGU Student Repository

Support
For questions or issues, please refer to the project's GitLab repository or contact the course instructor.


## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
